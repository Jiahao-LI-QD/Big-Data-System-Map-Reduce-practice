#!/usr/bin/python

import sys
import re

prev_line = ''

for line in sys.stdin:
    #check if there is a newline in "text"

    if re.search(r'\"\n|\"', line) is None:
        prev_line = prev_line + line
        continue
    #check if there is a previous line with newline
    if prev_line != '':
        line = prev_line + line
        prev_line = ''

    records = re.split( r'\",\"', line)
    text = records[0][1:]
    next = re.sub( r',|\. |\.$|\: |!|\，|\。|\！|\：'," ", text)
    print(next)
    words = next.split()

    for word in words :
        print( word.lower() + "\t1")
