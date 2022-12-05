#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

with open("input.txt", "r") as f:
    input_data = f.read()

crates, instructions = input_data.split("\n\n")

crates = [re.findall("....", f"{level} ") for level in reversed(crates.split("\n"))]

crate_stacks_1 = {}
crate_stacks_2 = {}
for k in crates[0]:
    crate_stacks_1[int(k.strip())] = []
    crate_stacks_2[int(k.strip())] = []
crates = crates[1:]

for crate_line in crates:
    crate_line = [crate.strip() for crate in crate_line]
    for n, crate in enumerate(crate_line):
        if crate != "":
            crate_stacks_1[n+1].append(crate)
            crate_stacks_2[n+1].append(crate)

for instruction in instructions.split("\n"):
    n, from_stack, to_stack = [int(i) for i in re.match(r"move (\d+) from (\d+) to (\d+)", instruction).groups()]
    # mover 9000
    for _ in range(n):
        crate_stacks_1[to_stack].append(crate_stacks_1[from_stack].pop())
    # mover 9001
    crate_stacks_2[to_stack].extend(crate_stacks_2[from_stack][-n:])
    for _ in range(n):
        crate_stacks_2[from_stack].pop()

solution_1 = []
solution_2 = []
for stack_number in crate_stacks_1.keys():
    solution_1.append(crate_stacks_1[stack_number][-1].strip("[]"))
    solution_2.append(crate_stacks_2[stack_number][-1].strip("[]"))

print(f"Solution to part 1: {''.join(solution_1)}")
print(f"Solution to part 2: {''.join(solution_2)}")