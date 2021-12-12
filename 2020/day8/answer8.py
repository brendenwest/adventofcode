lines = [n.strip('\n').split() for n in open("input.txt", "r").readlines()]

# prepare data
for i, line in enumerate(lines):
    line[1] = int(line[1])
    line.append(False)
    lines[i] = line

def part_one():
    acc = 0
    valid = True
    n = 0
    count = 0
    while valid:
        count += 1
        if lines[n][2]:
            break
        lines[n][2] = count
        if lines[n][0] == 'acc':
            acc += lines[n][1]
            n += 1
        elif lines[n][0] == 'nop':
            n += 1
        else:   # jump
            n += lines[n][1]

    print('Total',acc)

def part_two():
    acc = 0
    valid = True
    current = 0
    count = 0
    has_jumped = False
    while valid:
        count += 1
        if lines[current][2]:
            print()
            print(current, lines[current])
            break
        lines[current][2] = count
        print()
        print(current, lines[current])
        if lines[current][0] == 'acc':
            acc += lines[current][1]
            current += 1
        elif lines[current][0] == 'nop':
            current += 1
        else:   # jump
            if has_no_opped and has_jumped and not_flip:

            elif lines[current][1] < 0:
                lines[current][0] = 'nop'
                current += 1
                has_no_opped = True
            else:
                print('jump')
                has_jumped = True
                current += lines[current][1]

        if current == len(lines):
            break

    print('Total', acc)

#part_one()
part_two()
'''
wrong - 624, 2668
'''
#print(lines)
