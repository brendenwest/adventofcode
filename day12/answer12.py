moves = [line.strip('\n') for line in open("input.txt", "r").readlines()]

directions = ['E','S','W','N']
rotation = {'L': -1, 'R': 1}

def manhattan(x,y):
    return abs(x) + abs(y)

cur_dir = 'E'
x = 0
y = 0
for move in moves:
    action = move[:1]
    val = int(move[1:])

    if action == 'F':
        action = cur_dir

    if action == 'R' or action == 'L':
        start = directions.index(cur_dir)
        change = rotation[action] * val // 90
        cur_dir = directions[(start + change) % 4]

    if action == 'N':
        y += val
    elif action == 'S':
        y -= val
    elif action == 'E':
        x += val
    elif action == 'W':
        x -= val

print(x, y)
print('Manhattan', manhattan(x,y))