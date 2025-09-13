import re

PATTERN = re.compile(r"ArubaOS \(MODEL: ([^\)]+)\), Version (8\.[^\s]+)")
SNMP_DESCRIPTION = "ArubaOS (MODEL: Aruba9004), Version 8.7.0.0-2.3.0.4 (82267)"

result = PATTERN.match(SNMP_DESCRIPTION)
print(result.group(1))
print(result.group(2))
