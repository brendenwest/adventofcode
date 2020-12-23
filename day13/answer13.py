with open("input.txt", "r") as f:
    start = int(f.readline())
    busses = {int(b):[] for b in f.readline().strip('\n').split(',') if b != 'x'}

end = start + max(busses.keys()) + 1
# compile bus schedules
for bus in busses.keys():
    busses[bus] = range(0,end,bus)

arrival = None
my_bus = None
# which bus arrives soonest
for n in range(start,end):
    if arrival:
        break
    for bus in busses:
        if n in busses[bus]:
            arrival = n
            my_bus = bus
            print('Bus {0}'.format(bus), n, )
            break

wait = arrival - start
print('wait time', wait)
print('answer', my_bus * wait)