import sys
sys.path.append('../utils')
from utils import input

# part 1
def get_priority(letter):
    letters = " abcdefghijklmnopqrstuvwxyz"
    priority = letters.find(letter)
    if priority < 0:
        priority = letters.find(letter.lower())+26
    return priority

sum = 0
for line in input():
    mid = len(line)//2
    a = set(line[0:mid])
    b = set(line[mid:])
    overlap = a.intersection(b)
    for x in overlap:
        sum += get_priority(x)
print("part 1", sum)

# part 2
count = 0
group = []
sum = 0
for line in input():
    group.append(line.strip())
    count += 1
    if count == 3:
        sets = [set(part) for part in group]
        badge = sets[0].intersection(sets[1]).intersection(sets[2])
        for x in badge:
            sum += get_priority(x)
        count = 0
        group = []

print("part 2", sum)