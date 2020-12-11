lines = open("input.txt", "r").readlines()
#lines = open("sample.txt", "r").readlines()
#lines = open("sample2.txt", "r").readlines()

# prepare data
for i, line in enumerate(lines):
    line = line.replace('\n','').split()
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
    last_jump = 0
    while valid:
        count += 1
#        print(count, 'cur', current)
#        print(lines)
        print()

        lines[current][2] = count
        print(current, lines[current])
        if lines[current][0] == 'acc':
            acc += lines[current][1]
            current += 1
        elif lines[current][0] == 'nop':
            current += 1
        else:   # jump
            if last_jump:
                lines[current][0] = 'nop'
                current += 1
            else:
                print('jump')
                last_jump = lines[current][1]
                current += lines[current][1]


        if current == len(lines):
            break

    print('Total', acc)

#part_one()
part_two()
#print(lines)
