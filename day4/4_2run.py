f = open('input.txt', 'r')
raw = f.read()
raw = raw.split('\n\n')
entries = [ entry.strip().replace('\n', ' ').split() for entry in raw]
print(f"A total of {len(entries)} entries in this data.")
import re
rules = {
    'byr': r'(19[2-9]\d|200[0-2])',#1920 - 2002
    'iyr': r'(201\d|2020)',#2010-2020
    'eyr': r'(202\d|2030)',
    'hgt': r'((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)',
    'hcl': r'#[0-9a-f]{6}',
    'ecl': r'(amb|blu|brn|gry|grn|hzl|oth)',
    'pid': r'^[0-9]{9}$'
        }
num_passport = 0
num = 0
for entry in entries:
    num_valid_field = 0
    fields = [ field.split(':') for field in entry ]
    for field in fields:
        #print(field)
        if field[0] == 'cid':
            continue
        p = re.compile(rules[field[0]])
        m = p.match(str(field[1]))
        if m:
            num_valid_field += 1
    if num_valid_field == 7:
        num_passport += 1
print(num_passport)
