import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.fullmatch('(1(01*0)*1|0)*0', line):
        print(line)
