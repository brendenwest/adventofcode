
# part 1
max = (0, 0)
count = 0
sum = 0
for line in open("input.txt", "r").readlines():
    if len(line) > 1:
        sum += int(line)
    else:
        if sum > max[1]:
            max = (count, sum)
        sum = 0
        count += 1

print("part 1", max)

# part 2
import heapq, functools
h = []
count = 0
sum = 0
for line in open("input.txt", "r").readlines():
    if len(line) > 1:
        sum += int(line)
    else:
        heapq.heappush(h, sum)
        sum = 0
        count += 1

print("part 2", functools.reduce(lambda x, y: x+y, heapq.nlargest(3,h)))