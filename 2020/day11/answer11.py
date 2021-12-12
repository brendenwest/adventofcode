grid = [[c for c in line.strip('\n')] for line in open("input.txt", "r").readlines()]

right_col = len(grid[0])-1
bottom_row = len(grid)-1

def printg(grid):
    for row in grid:
        print(''.join(row))

#printg(grid)

print()

def occupied_neighbors(grid, row,col):
    neighbors = 0
    # if cell has left neighbor
    if col >  0:
#        print('left', grid[row][col-1])
        neighbors += bool(grid[row][col-1] == '#')

    # if cell has right neighbor
    if col < right_col:
#        print('right', grid[row][col+1])
        neighbors += bool(grid[row][col+1] == '#')

    # if cell has top neighbor
    if row > 0:
#        print('top', grid[row-1][col])
        neighbors += bool(grid[row-1][col] == '#')

    # if cell has bottom neighbor
    if row < bottom_row:
#        print('bottom', grid[row+1][col])
        neighbors += bool(grid[row+1][col] == '#')

    # if cell has upper left neighbor
    if col >  0 and  row > 0:
#        print('upper left', grid[row-1][col-1])
        neighbors += bool(grid[row-1][col-1] == '#')

    # if cell has lower left neighbor
    if col >  0 and row < bottom_row:
#        print('lower left', grid[row+1][col-1])
        neighbors += bool(grid[row+1][col-1] == '#')

    # if cell has upper right neighbor
    if col < right_col and row > 0:
#        print('upper right', grid[row-1][col+1])
        neighbors += bool(grid[row-1][col+1] == '#')

    # if cell has lower right neighbor
    if col < right_col and row < bottom_row:
#        print('lower right', grid[row+1][col+1])
        neighbors += bool(grid[row+1][col+1] == '#')

    return neighbors

def apply_rules(grid):
    new_grid = [[None for _ in grid[0]] for _ in range(len(grid))]
    changed = 0
    occupied = 0
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == '.':
                new_grid[r][c] = '.'
            else:
                occ = occupied_neighbors(grid, r, c)
                if val == 'L' and occ == 0:
                    new_grid[r][c] = '#'
                    changed += 1
                    occupied += 1
                elif val == '#' and occ >= 4:
                    new_grid[r][c] = 'L'
                    changed += 1
                else:
                    new_grid[r][c] = val
                    if val == '#':
                        occupied += 1
    return changed, occupied, new_grid

changed = len(grid)*len(grid[0])
while changed > 0:
    changed, occupied, grid = apply_rules(grid.copy())
    print('changed', changed)
    print('occupied', occupied)
#    printg(grid)
    print()

