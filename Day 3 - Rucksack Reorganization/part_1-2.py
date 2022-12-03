#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

def get_prio(c):
    if c.isupper():
        return(ord(c)-38)
    else:
        return(ord(c)-96)

rucksack_list = []
with open("input.txt", "r") as f:
    for r in f.readlines():
        r = r.strip()
        rucksack_list.append([r[0:int(len(r)/2)], r[int(len(r)/2):]])

priority = 0
for cmp_1, cmp_2 in rucksack_list:
    p = [l for l in cmp_1 if l in cmp_2][0]
    if p.isupper():
        priority += ord(p)-38
    else:
        priority += ord(p)-96

print(f"Answer to part 1: {priority}")

priority = 0
for i in range(0, len(rucksack_list), 3):
    r_1 = "".join(rucksack_list[i])
    r_2 = "".join(rucksack_list[i+1])
    r_3 = "".join(rucksack_list[i+2])
    p = [l for l in r_1 if l in r_2 and l in r_3][0]
    priority += get_prio(p)

print(f"Answer to part 2: {priority}")