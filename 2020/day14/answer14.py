import re
import functools

f = open("input.txt", "r")
mask = None
mem = {}
total = 0
def binary_to_int(num):
    return int("".join(num), 2)

def apply_mask(num):
    new_num =[]
    for i, c in enumerate(f'{int(num):036b}'):
        if mask[i] == 'X' or mask[i] == c:
            new_num.append(c)
        else:
            new_num.append(mask[i])
#    print("".join(new_num))
    # return base-10 number
    return binary_to_int(new_num)

for line in f.readlines():
    command = line.strip('\n').split(' = ')
    if command[0] == 'mask':
        mask = command[1]
        print(mask)
    else:
        print(command[1])
        new_num = apply_mask(command[1])
        print(new_num)

        mem_pos = re.search("[0-9]+", command[0]).group()
        mem[int(mem_pos)] = new_num

#print(mem)
total = functools.reduce(lambda a,b : a+b,mem.values())
print('Total',total)

