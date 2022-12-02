#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("input.txt", "r") as f:
    strategy_guide = [r.strip() for r in f.readlines()]

# R > P > S > R
score_table = {
    "A X" : 1+3,
    "A Y" : 2+6,
    "A Z" : 3+0,
    "B X" : 1+0,
    "B Y" : 2+3,
    "B Z" : 3+6,
    "C X" : 1+6,
    "C Y" : 2+0,
    "C Z" : 3+3
}
print(sum([score_table[r] for r in strategy_guide]))

# lose, draw, win
strategy_table = {
    "A X" : "A Z",
    "A Y" : "A X",
    "A Z" : "A Y",
    "B X" : "B X",
    "B Y" : "B Y",
    "B Z" : "B Z",
    "C X" : "C Y",
    "C Y" : "C Z",
    "C Z" : "C X"
}
print(sum([score_table[strategy_table[r]] for r in strategy_guide]))