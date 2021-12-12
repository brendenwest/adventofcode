with open("input.txt", "r") as f:
    start = int(f.readline())
    buslist = f.readline().strip('\n').split(',')

def part1():
    buses = {int(b):[] for b in buslist if b != 'x'}
    end = start + max(buses.keys()) + 1
    # compile bus schedules
    for bus in buses.keys():
        buses[bus] = range(0,end,bus)

    arrival = None
    my_bus = None
    # which bus arrives soonest
    for n in range(start,end):
        if arrival:
            break
        for bus in buses:
            if n in buses[bus]:
                arrival = n
                my_bus = bus
                print('Bus {0}'.format(bus), n, )
                break

    wait = arrival - start
    print('wait time', wait)
    print('answer', my_bus * wait)

#part1()

# part 2 test cases
#buslist = '17,x,13,19'.split(',')   # 3417
#buslist = '67,7,59,61'.split(',')   # 754018
#buslist = '67,x,7,59,61'.split(',') # 779210
#buslist = '67,7,x,59,61'.split(',') # 1261476
#buslist = '1789,37,47,1889'.split(',') # 1202161486

max_bus = 0
max_pos = -1
bus_count = 0
buses = {}
for i, b in enumerate(buslist):
    if b != 'x':
        num = int(b)
        buses[num] = i
        if num > max_bus:
            max_bus = num
            max_pos = i

print(buses)
print(max_bus, max_pos)
bus_count = len(buses)
t = max_bus

# https://www.geeksforgeeks.org/chinese-remainder-theorem-set-2-implementation/
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

nums = buses.keys()
remainders = []
for b in buses:
    delta = max_pos - buses[b]
    if delta < 0:
        remainders.append(b+delta)
    else:
        remainders.append(delta)

# fast solution
match = chinese_remainder(nums, remainders)
print('match',match)
matches = [match+(v-max_pos) for v in buses.values()]
print(matches)
print('earliest', min(matches))