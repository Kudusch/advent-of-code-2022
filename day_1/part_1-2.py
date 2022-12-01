#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("input.txt", "r") as f:
    inventory_list = f.read()

inventory_list = [inventory.split("\n") for inventory in inventory_list.split("\n\n")]

inventory_list_totals = []
for inventory in inventory_list:
    inventory_list_totals.append(sum([int(e) for e in inventory]))

inventory_list_totals.sort()

print(f"The Elf carrying the most Calories carries {inventory_list_totals[-1]} calories")
print(f"The top three Elves carrying the most Calories carrie {sum(inventory_list_totals[-3:])} calories")

