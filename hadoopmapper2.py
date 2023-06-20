#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    word, doc, count = line.split('\t')
    key = word
    val = "{}={}".format(doc, count)
   
    print("{}\t{}".format(key, val))