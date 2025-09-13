import asyncio
from pysnmp.hlapi.v3arch.asyncio import (
    SnmpEngine, CommunityData, UdpTransportTarget, ContextData,
    ObjectType, ObjectIdentity, get_cmd
)

HOST = "" # Put IP address here
PORT_NUMBER = 161

async def main():
    *_, varBinds = await get_cmd(
        SnmpEngine(),
        CommunityData("public"),
        await UdpTransportTarget.create((HOST, PORT_NUMBER)),
        ContextData(),
        ObjectType(ObjectIdentity("1.3.6.1.2.1.1.1.0"))
    )
    print(varBinds[0][1])

if __name__ == "__main__":
    asyncio.run(main())
