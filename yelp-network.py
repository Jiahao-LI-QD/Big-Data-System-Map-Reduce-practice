import sys
import csv
import os

if len(sys.argv) <= 1:
    print("Valid parameters needed!")
    exit()

maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

out = open("yelp-network.txt","w")    
filename = sys.argv[1]
l = set()

with open(filename, 'r', encoding='UTF-8') as f:
#with open(filename) as f:
    csv_read = csv.reader(f)
    title = next(csv_read)
    for line in csv_read:
        l.add(line[0])
        if line[4] == "None":
            continue
        fs = line[4].split(', ')
        setf = set(fs) - l
        #pure = list(set(fs).difference(set(l)))
        for u in setf:    
            out.write("%s %s\n" % (line[0],u))

out.close()
        
        
        
