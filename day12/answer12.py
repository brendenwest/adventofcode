moves = [line.strip('\n') for line in open("input.txt", "r").readlines()]

directions = ['E','S','W','N']
rotation = {'L': -1, 'R': 1}

def manhattan(x,y):
    return abs(x) + abs(y)

def parse_move(move):
    return move[:1], int(move[1:])

def rotate(cur_dir, action, val):
    start = directions.index(cur_dir)
    change = rotation[action] * val // 90
    return directions[(start + change) % 4]

def part1():
    cur_dir = 'E'
    x = 0
    y = 0
    for move in moves:
        action, val = parse_move(move)

        if action == 'F':
            action = cur_dir

        if action == 'R' or action == 'L':
            cur_dir = rotate(cur_dir, action, val)

        if action == 'N':
            y += val
        elif action == 'S':
            y -= val
        elif action == 'E':
            x += val
        elif action == 'W':
            x -= val

    print('X:',x, 'Y:',y)
    print('Manhattan', manhattan(x,y))

def part2():
    cur_dir = 'E'
    x = 0
    y = 0
    wp = [10, 1]

    for move in moves:
        action, val = parse_move(move)

        if action == 'F':
            #  move forward to the waypoint a number of times equal to the given value.
            x += val * wp[0]
            y += val * wp[1]

        if action == 'R' or action == 'L':
            # clockwise
            if (val == 90 and action == 'R') or (val == 270 and action == 'L'):
                wp = [wp[1], wp[0]*-1]
            # counter-clockwise
            elif (val == 90 and action == 'L') or (val == 270 and action == 'R'):
                wp = [wp[1]*-1, wp[0]]
            elif val == 180:
                wp = [wp[0]*-1, wp[1]*-1]

        if action == 'N':
            wp[1] += val
        elif action == 'S':
            wp[1] -= val
        elif action == 'E':
            wp[0] += val
        elif action == 'W':
            wp[0] -= val

        # print(move)
        # print(wp)
        # print()

    print('X:',x, 'Y:',y)
    print('WP_X:', wp[0], 'WP_Y:', wp[1])
    print('Manhattan', manhattan(x,y))

part1()
print()
part2()

