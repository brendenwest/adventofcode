import re
text = open("input.txt", "r").read()
blocks = text.split('\n\n')
count = 0
valid = 0

def valid_height(val):
    num = ''.join([s for s in val if s.isdigit()])
    if val.find('in') > 0 and int(num) in range(59,77):
        return True
    if val.find('cm') > 0 and int(num) in range(150,194):
        return True

for block in blocks:
    block = block.replace('\n', ' ')
    passport = {x.split(':')[0]:x.split(':')[1] for x in block.split()}

    # valid if all 8 fields
    if len(passport) == 8 or (len(passport) == 7 and not passport.get('cid')):
        if int(passport['byr']) not in range(1920, 2003):
            continue
        if int(passport['iyr']) not in range(2010, 2021):
            continue
        if int(passport['eyr']) not in range(2020, 2031):
            continue
        if not valid_height(passport['hgt']):
            continue

        match = re.search("^#.[0-9,abcdef]+", passport['hcl'])
        if not match or len(match.string) != 7:
            continue
        if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue

        pid = re.search("^[0-9]+", passport['pid'])
        if not pid or len(pid.string) != 9:
            continue

        valid += 1

    count += 1

print('valid =', valid)