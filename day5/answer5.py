lines = open("input.txt", "r").readlines()

def get_row(val):
    lo = 0
    hi = 128
    for c in val:
        mid = int(hi - 0.5* (hi - lo))
        if c == 'F':  # choose lower half of range
            hi = mid
        else:
            lo = mid
    return lo

def get_col(val):
    lo = 0
    hi = 8
    for c in val:
        mid = int(hi - 0.5* (hi - lo))
        if c == 'L':  # choose lower half of range
            hi = mid
        else:
            lo = mid
    return lo


'''
FBFBBFFRLR: row 44, column 5, seat ID 357
BFFFBBFRRR: row 70, column 7, seat ID 567
FFFBBBFRRR: row 14, column 7, seat ID 119
BBFFBBFRLL: row 102, column 4, seat ID 820
'''

'''
print(get_row('FBFBBFF'))
print(get_row('BFFFBBF'))
print(get_row('FFFBBBF'))
print(get_row('BBFFBBF'))

print(get_col('RLR'))
print(get_col('RRR'))
print(get_col('RLL'))
'''
max = 0
rows = 128
cols = 8
seat_ids = [False] * rows*cols + [False,False,False,False,False]

for line in lines:
    # id = row * 8 + col
    row = get_row(line[:7])
    col = get_col(line[7:10])
    id = row * cols + col
    seat_ids[id] = True

    if id > max:
        max = id

print('Highest seat:', max)

# my seat
for id, val in enumerate(seat_ids):
    if not val and (seat_ids[id-1] and seat_ids[id+1]):
        print('My seat:', id)
        break

