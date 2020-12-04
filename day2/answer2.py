lines = open("input.txt", "r").readlines()

# check valid passwords

# letter must be between 1st & 2nd numbers
# 1-13 r: gqdrspndrpsrjfjx
valid = 0
for line in lines:
    parts = line.split()
    lo, hi = parts[0].split('-')
    value = parts[1].rstrip(':')
    count = parts[2].count(value)
    if count in range(int(lo), int(hi)+1):
        valid += 1
print(valid)

# letter must be 1st or 2nd position but not both
# 1-13 r: gqdrspndrpsrjfjx
valid = 0
for line in lines:
    parts = line.split()
    pos1, pos2 = parts[0].split('-')
    value = parts[1].rstrip(':')
    pos1 = int(pos1)-1
    pos2 = int(pos2)-1
    count = int(parts[2][pos1] == value) + int(parts[2][pos2] == value)
    if count == 1:
        valid += 1
print(valid)
