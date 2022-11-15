import sys
import csv
import os
from collections import defaultdict
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
  
filename = sys.argv[1]
dic = {}
dic = defaultdict(lambda:0, dic)
edges = 0

if len(sys.argv) < 3:
    out = "nodeDegreeDist.txt"
else:
    out = sys.argv[2]

with open(filename, 'r', encoding='UTF-8') as f:
#with open(filename) as f:
    for line in f:
        edges += 1
        nodes = line.split(' ')
        nodes[1] = ( nodes[1].split('\n') )[0]
        dic[nodes[0]] += 1
        dic[nodes[1]] += 1

#print
print("#nodes:%d #edges:%d" % (len(dic), edges))

#sort
sorted_dic = {}
sorted_dic_key = sorted(dic, key=dic.get, reverse=True)
for key in sorted_dic_key:
    sorted_dic[key] = dic[key]

nodeDegreeDist = open(out,"w")
for n in sorted_dic:
    nodeDegreeDist.write("%s:%d\n" % (n, sorted_dic[n]))
nodeDegreeDist.close()

avgNodeDegree = 2 * edges / len(dic)
print("avgNodeDegree:%.2f" % (avgNodeDegree) )
