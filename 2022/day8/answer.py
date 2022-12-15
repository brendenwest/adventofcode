import sys
sys.path.append('../utils')
from utils import input

grid = []
for line in input():
    line = line.strip()
    grid.append([int(c) for c in line])

def get_vis(current, list):
    for tree in list:
        if tree >= current:
            return False
    return True

def get_distance(current, list, reverse=False):
    distance = 0
    if reverse:
        list.reverse()
    for tree in list:
        distance += 1
        if tree >= current:
            break

    return distance

size = len(grid)
visible = 0
for row in range(size):
    for col in range(size):
        if row ==0 or col == 0 or row == size-1 or col == size -1:
            visible += 1
        else:
            # check interior trees
            current_tree = grid[row][col]
            left = get_vis(current_tree, grid[row][:col])
            right = get_vis(current_tree, grid[row][col+1:])
            top = get_vis(current_tree, [grid[val][col] for val in range(row)])
            bottom = get_vis(current_tree, [grid[val][col] for val in range(row+1,size)])

            if left or right or top or bottom:
                visible += 1

print('visible', visible)

# part 2
max_score=0
for row in range(size):
    for col in range(size):
        current_tree = grid[row][col]
        grid[row][:col].reverse()
        left = get_distance(current_tree, grid[row][:col], True)
        right = get_distance(current_tree, grid[row][col+1:])
        top = get_distance(current_tree, [grid[val][col] for val in range(row)], True)
        bottom = get_distance(current_tree, [grid[val][col] for val in range(row+1,size)])

        score = left * right * top * bottom

        if score > max_score:
            max_score = score

print('max score', max_score)