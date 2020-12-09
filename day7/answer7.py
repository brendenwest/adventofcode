lines = open("input.txt", "r").readlines()
#lines = open("sample2.txt", "r").readlines()

bags = {}
# construct bags collection
for i, line in enumerate(lines):
    text = line.replace(' bags','').replace('.\n','')\
        .replace(' bag','').replace('no','0')\
        .split(' contain ')

    values = text[1].split(', ')
    bags[text[0]] = {x[2:]:x[:1] for x in values}

# determine if a bag can contain another bag
def find_path(collection, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not collection.get(start):
        return None
    for node in collection[start]:
        if node not in path:
            newpath = find_path(collection, node, end, path)
            if newpath: return newpath
    return None

# count # of bags that can contain target bag
def get_matches(start):
    matches = set()
    for bag in bags:
        if bag != start and find_path(bags, bag, start):
            matches.add(bag)
    return matches

print(len(get_matches('shiny gold')))

# count # of bags target can contain
def count_bags(parent):
    b = bags[parent]
    count = 1
    for key in b.keys():
        val = int(b[key])
        if val > 0:
            count += val * count_bags(key)
    return count

print(count_bags('shiny gold'))


'''
bags = {
    'light beige': {
        'dark green': 5,
        'light gray': 5,
        'faded indigo': 3,
        'vibrant aqua': 2,
    },
    'vibrant beige': {
        'pale silver': 1
    }
}
'''