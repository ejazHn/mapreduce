#!/usr/bin/env python
import sys

def get_input_file_name():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "Unknown"

def trim_and_lower_case(s):
    return s.strip().lower()

for line in sys.stdin:
    doc = get_input_file_name()
    line = trim_and_lower_case(line)
    words = line.split()
   
    for word in words:
        print(f"{word}\ts\t1\t{doc}")