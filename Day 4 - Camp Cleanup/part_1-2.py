#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("input.txt", "r") as f:
    assignment_pairs = [assignment_pair.strip().split(",") for assignment_pair in f.readlines()]

def make_range(assignment):
    start, stop = assignment.split("-")
    return range(int(start), int(stop)+1)

def is_fully_contained(assignment_pair):
    assignment_1, assignment_2 = [make_range(assignment) for assignment in assignment_pair]
    if len(assignment_1) > len(assignment_2):
        return ((min(assignment_1) <= min(assignment_2)) and (max(assignment_1) >= max(assignment_2)))
    elif len(assignment_2) > len(assignment_1):
        return ((min(assignment_2) <= min(assignment_1)) and (max(assignment_2) >= max(assignment_1)))
    elif assignment_pair[0] == assignment_pair[1]:
        return True
    else:
        return False


def is_overlapped(assignment_pair):
    assignment_1, assignment_2 = [make_range(assignment) for assignment in assignment_pair]
    return any([i in assignment_2 for i in assignment_1])

solution_1 = 0
solution_2 = 0
for assignment_pair in assignment_pairs:
    if is_fully_contained(assignment_pair):
        solution_1 += 1
    if is_overlapped(assignment_pair):
        solution_2 += 1

print(solution_1)
print(solution_2)