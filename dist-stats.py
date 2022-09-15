import sys
import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) <= 2:
    print("Valid parameters needed!")
    exit()

def res(str):
    l = str.split(';')
    for i in l:
        if i == "Restaurants":
            return True
    return False
    
filename = sys.argv[1]
city = sys.argv[2]

restaurantCategoryDist = {}
restaurantReviewDist = {}
restaurantStarsDist = {}

with open(filename) as f:
    csv_read = csv.reader(f)
    title = next(csv_read)
    for line in csv_read:
        dic = dict(zip(title, line))
        if dic["city"] == city:
            if res(dic["categories"]):
                cates = dic["categories"].split(';')
                for c in cates:
                    if c == "Restaurants":
                        pass
                    else:
                        if c in restaurantCategoryDist:
                            restaurantCategoryDist[c] += 1
                            restaurantReviewDist[c] += float(dic["review_count"])
                            restaurantStarsDist[c] += float(dic["stars"])
                        else:
                            restaurantCategoryDist[c] = 1
                            restaurantReviewDist[c] = float(dic["review_count"])
                            restaurantStarsDist[c] = float(dic["stars"])
                #float(dic["stars"])
                #float(dic["review_count"])

restaurantAvgStarsDist = {}
for x, y in restaurantStarsDist.items():
    restaurantAvgStarsDist[x] = y / restaurantCategoryDist[x]

#sort

#print


#barchart
top10 = []
y_count = []
i = 0
for c in restaurantCategoryDist:
    if i == 10:
        break
    top10.append(c)
    y_count.append(restaurantCategoryDist[c])
    i += 1
    
objects = tuple(top10)
y_pos = np.arange(len(objects))

plt.bar(y_pos, y_count, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Frequency')
plt.title('Restaurant Category Distribution')

plt.show()
