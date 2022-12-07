#!/usr/bin/env python
# -*- coding: utf-8 -*-

from anytree import Node, RenderTree, PreOrderIter

def path_to_string(node):
    return "/".join([n.name for n in node.path])

def get_size(dir_node):
    if dir_node.meta != "dir":
        return int(dir_node.meta)
    else:
        size = 0
        for n in dir_node.children:
            size += get_size(n)
        return size
        

with open("input.txt", "r") as f:
    commands = [c.strip() for c in f.readlines()]

root = Node("root", meta = "dir")
pwd = root
for c in commands[1:]:
    c = c.split(" ")
    if c[0] == "$" and c[1] == "ls":
        continue
    elif c[0] == "$" and c[1] == "cd":
        if c[2] == "..":
            pwd = pwd.parent
        else:
            pwd = [n for n in pwd.children if n.name == c[2]][0]
    else:
        new_node = Node(c[1], parent=pwd, meta=c[0])

for pre, fill, node in RenderTree(root):
    print("%s%s (%s)" % (pre, node.name, node.meta))

dir_list = {}
for n in PreOrderIter(root):
    if n.meta == "dir":
        dir_list[path_to_string(n)] = get_size(n)

solution_1 = 0
for size in dir_list.values():
    if size <= 100000:
        solution_1 += size

print(f"The sum of the total sizes of directories with a total size of at most 100000 is: {solution_1}")

free_space = 70000000-dir_list['root']

print(f"There is {free_space} of unused space.")
print(f"The smallest directory with at least the size of {30000000-free_space} must be deleted:")

deletion_candidates = dict(filter(lambda val: val[1] >= (30000000-free_space), dir_list.items()))
smallest_candidate = min(deletion_candidates, key=deletion_candidates.get)
for n,s in deletion_candidates.items():
    if n == smallest_candidate:
        print("- %s (size=%s) <- smallest" % (n, s))
    else:
        print("- %s (size=%s)" % (n, s))