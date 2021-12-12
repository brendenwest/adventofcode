adapters = [int(n.strip('\n')) for n in open("sample.txt", "r").readlines()]
#print(adapters)
adapters.sort()

# add built-in adapter
last = adapters[len(adapters)-1]
adapters.append(last + 3)

def get_differences():
    outlet = 0
    differences = []
    for adapter in adapters:
        diff = adapter - outlet
        if diff < 4:
            differences.append(diff)
            outlet = adapter
    return differences

#print(differences)
differences = get_differences()
ones = differences.count(1)
threes = differences.count(3)
# print('Ones', ones)
# print('Threes', threes)
print("Product", ones*threes)

found = [adapters]

def arrange(sequence, skip_index):
    index = 0
    for _ in sequence:
        index += 1
        if index not in skip_index and index < len(sequence)-1:   # ignore last item
            if sequence[index+1] - sequence[index-1] < 4:
                sequence.pop(index)
                return index, sequence

    return index, sequence

def _get_arrangements(sequence, skip_index):
    count = len(sequence)
    removed, new_list = arrange(sequence,skip_index)

    if len(new_list) == count:
        print('done')
        print(skip_index)
        return removed, new_list
    else:
        print('skip', skip_index, 'removed', removed)
        print(new_list)
        sequence = new_list
        return get_arrangements(sequence,skip_index)


def get_arrangements(sequence, skip_index):
    first_removed = None
    while True:
        count = len(sequence)
        removed, new_list = arrange(sequence,skip_index)
        if not first_removed:
            first_removed = removed

        if len(new_list) == count:
            return first_removed
        else:
            print('skip', skip_index, 'removed', removed)
            print(new_list)
            found.append(new_list.copy())
            sequence = new_list


expected = [
    [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22],
    [1, 4, 5, 6, 7, 10, 12, 15, 16, 19, 22],
    [1, 4, 5, 7, 10, 11, 12, 15, 16, 19, 22],
    [1, 4, 5, 7, 10, 12, 15, 16, 19, 22],
    [1, 4, 6, 7, 10, 11, 12, 15, 16, 19, 22],
    [1, 4, 6, 7, 10, 12, 15, 16, 19, 22],
    [1, 4, 7, 10, 11, 12, 15, 16, 19, 22],
    [1, 4, 7, 10, 12, 15, 16, 19, 22]
]

count = 0

skip_index = [0]
removed = get_arrangements(adapters.copy(), skip_index)

skip_index.append(removed)
removed = get_arrangements(adapters.copy(), skip_index)

skip_index.append(removed)
removed = get_arrangements(adapters.copy(), skip_index)

skip_index.pop(1)
removed = get_arrangements(adapters.copy(), skip_index)

'''
first_removed = None
while True:
    count = len(sequence)
    removed, new_list = arrange(sequence.copy(),skip_index)
    if not first_removed:
        first_removed =  removed
    print(new_list)
    if len(new_list) == count:
        print('done')
        break
    else:
        found.append(new_list)
        print('skip', skip_index, 'removed', removed)
        sequence = new_list

print(first_removed)
print('SECOND')
skip_index.append(first_removed)
sequence = adapters.copy()
first_removed = None
while True:
    count = len(sequence)
    removed, new_list = arrange(sequence.copy(),skip_index)
    if not first_removed:
        first_removed =  removed
    print(new_list)
    if len(new_list) == count:
        print('done')
        break
    else:
        found.append(new_list)
        print('skip', skip_index, 'removed', removed)
        sequence = new_list

print(first_removed)
print('THIRD')
skip_index.append(first_removed)
sequence = adapters.copy()
first_removed = None
while True:
    count = len(sequence)
    removed, new_list = arrange(sequence.copy(),skip_index)
    if not first_removed:
        first_removed =  removed
    print(new_list)
    if len(new_list) == count:
        print('done')
        break
    else:
        found.append(new_list)
        print('skip', skip_index, 'removed', removed)
        sequence = new_list
'''
# if removed > -1:
#     'SECOND'
#     skip_index.append(removed)
#     removed, sequence = get_arrangements(adapters.copy(), skip_index)
# if removed > -1:
#     'THIRD'
#     skip_index.append(removed)
#     removed, sequence = get_arrangements(adapters.copy(), skip_index)
    # print('ExTRA')
    # skip_index.pop(2)
    # print(skip_index)
    # removed, sequence = get_arrangements(adapters.copy(), skip_index)

print()
print(len(found))
print(found)
print('NOT FOUND')
for s in expected:
    if not s in found:
        print(s)


#get_arrangements(adapters.copy(), [0,2])
#get_arrangements(adapters.copy(), [0,3])
#get_arrangements(adapters.copy(), [0,2,3])
'''
(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)

(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)

(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)

(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)

(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)

(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)

(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)

(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)

'''

