#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open("input.txt", "r") as f:
    signal_stream = f.read()

def is_start_marker(word):
    return len(set(word)) == 4

def is_message_marker(word):
    return len(set(word)) == 14

for i in range(len(signal_stream)):
    if is_message_marker(signal_stream[i-14:i]):
        print(i)
        break
    # if is_start_marker(signal_stream[i-4:i]):
    #     print(i)
    #     break
