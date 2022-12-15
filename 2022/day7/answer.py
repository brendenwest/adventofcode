import functools
import sys
sys.path.append('../utils')
from utils import input

class Node():
    def __init__(self, name=None, size=0, parent=None):
        self.parent = parent
        self.children = []  # None if file, [] if folder
        self.name = name
        self.size = size

    def __repr__(self):
        return f'{self.name} - {self.size} - children: {[n.name for n in self.children]}'


def get_folder_size(node):
    if node.size:
        return node.size
    sum = 0
    for child in node.children:
        sum += get_folder_size(child)
    return sum

def get_node(root, name):
    for child in root.children:
        if child.name == name:
            return child

def get_folders_by_max(node, max=0, nodes=[]):
    if node.children:
        fsize = get_folder_size(node)
        if fsize <= max:
            nodes.append((node.name, fsize))
    for child in node.children:
         get_folders_by_max(child, max, nodes)
    return nodes

def get_folders_by_min(node, min=0, nodes=[]):
    if node.children:
        fsize = get_folder_size(node)
        if fsize >= min:
            nodes.append((node.name, fsize))
            for child in node.children:
                 get_folders_by_min(child, min, nodes)
    return nodes

root = current_node = Node("/")
for line in input():
    line = line.strip()
    if line[:4] == "$ cd":
        # command
        parts = line.split(" ")
        if parts[2] == "..":
            current_node = current_node.parent
        elif parts[2] != root.name:
            current_node = get_node(current_node, parts[2])
    elif line[0] == "$":
        pass
    elif line[:3] == "dir": # create directory node
        new_node = Node(line[4:], parent=current_node)
        current_node.children.append(new_node)
    elif int(line[0]):  # create file node
        parts = line.split(" ")
        new_node = Node(parts[1], int(parts[0]), parent=current_node)
        current_node.children.append(new_node)

# part 1
folders = get_folders_by_max(root, 100000)
total = functools.reduce(lambda a, b: a + b, [f[1] for f in folders])
print(total)

# part 2
total_space = 70000000
target = 30000000
root_size = get_folder_size(root)
unused = total_space - root_size
folders = get_folders_by_min(root, target - unused)
folders.sort(key = lambda x: x[1])
print(folders[0])