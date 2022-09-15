#!/usr/bin/python

import sys

prev = None
sum = 0

for line in sys.stdin:
    #split the line with \t
    key, value = line.split('\t')

    #check if there is a same key as the previous one
    if key != prev:
        if prev is not None:
            print( str(sum) + '\t' + prev)
        prev = key
        sum = 0
    sum = sum + int(value)

print( str(sum) + '\t' + str(prev))
