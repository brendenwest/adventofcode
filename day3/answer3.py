lines = open("input.txt", "r").readlines()

multiplier = len(lines)

# count trees
def count_trees(slope):
    line_num = 0
    trees = 0
    for i in range(0, len(lines), slope['y']):
        line = lines[i]
        full_line = line.rstrip('\n')*multiplier
        if line_num > 0:
            tmp = line.rstrip('\n')*4
            tree = full_line[line_num*slope['x']] =='#'
            trees += int(tree)
            if tree:
                tmp = tmp[:line_num*slope['x']] + 'X' + tmp[line_num*slope['x']:]
            else:
                tmp = tmp[:line_num*slope['x']] + 'O' + tmp[line_num*slope['x']:]
        line_num += 1
    return trees

a = count_trees({'x':1,'y':1})
b = count_trees({'x':3,'y':1})
c = count_trees({'x':5,'y':1})
d = count_trees({'x':7,'y':1})
e = count_trees({'x':1,'y':2})
print('Trees =', a) # 63
print('Trees =', b) # 254
print('Trees =', c) # 62
print('Trees =', d) # 56
print('Trees =', e) # 30

print('Total', a*b*c*d*e)
