import sys
sys.path.append('../utils')
from utils import input

lines = [
"    [D]           ",
"[N] [C]           ",
"[Z] [M] [P]       ",
" 1   2   3        ",
"                  ",
"move 1 from 2 to 1",
"move 3 from 1 to 3",
"move 2 from 2 to 1",
"move 1 from 1 to 2",
]

def stack_crates(line, stacks):
    crates = [line[4*i + 1:4*i + 2] for i in range(0,STACKS)]
    for num, crate in enumerate(crates):
        if len(stacks) < num+1:
            stacks.append([])
        if crate != ' ':
            stacks[num].append(crate)


part = 2
STACKS = 9
stacks = []
initialized = False
for line in input():
    # parse initial crates
    if not initialized:
        if line.find("1") > -1:
            initialized = True
            continue

        stack_crates(line, stacks)
    if initialized and line.find("move") == -1:
        for stack in stacks:
            stack.reverse()
    if initialized and line.find("move") > -1:
        # count = 1, stack1 = 3, stack2 = 5
        commands = line.strip().split(' ')
        count = int(commands[1])
        source = stacks[int(commands[3])-1]
        target = stacks[int(commands[5])-1]
        if part == 1:
            for i in range(count):
                crate = source.pop()
                target.append(crate)
        elif part == 2:
            crates = []
            for i in range(count):
                 crates.append(source.pop())
            for crate in crates[::-1]:
                 target.append(crate)
for stack in stacks:
    print(stack.pop(), end="")
print()