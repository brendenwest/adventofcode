
# sample data
lines = [
"2-4,6-8",
"2-3,4-5",
"5-7,7-9",
"2-8,3-7",
"6-6,4-6",
"2-6,4-8"
]

def data(is_test=False):
    if is_test:
        return lines
    return open("input.txt", "r").readlines()

# part 1
count = 0
for line in data():
    parts = line.strip().split(",")
    pairs = [part.split("-") for part in parts]
    if int(pairs[0][0]) <= int(pairs[1][0]) and int(pairs[0][1]) >= int(pairs[1][1]):
        count += 1
    elif int(pairs[1][0]) <= int(pairs[0][0]) and int(pairs[1][1]) >= int(pairs[0][1]):
        count += 1

print("part 1 =", count)

# part 1
count = 0
for line in data():
    parts = line.strip().split(",")
    pairs = [range(int(section[0]),int(section[1])+1) for section in [part.split("-") for part in parts]]
    if pairs[0].start in pairs[1] or pairs[0].stop-1 in pairs[1]:
        count += 1
    elif pairs[1].start in pairs[0] or pairs[1].stop-1 in pairs[0]:
        count += 1

print("part 2 =", count)
