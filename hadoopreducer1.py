#!/usr/bin/env python
import sys

current_key = None
current_count = 0
key = None

for line in sys.stdin:
    line = line.strip()
    word, doc, count = line.split('\t')
    key = word + '\t' + doc
   
    if current_key == key:
        current_count += 1
    else:
        if current_key is not None:
            print("%s\t%s" % (current_key, current_count))
        current_key = key
        current_count = int(count)

if current_key == key:
    print("%s\t%s" % (current_key, current_count))