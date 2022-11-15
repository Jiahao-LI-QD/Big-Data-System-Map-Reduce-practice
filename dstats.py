import sys
import csv
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

numOfBus = 0
avgStars = 0.0
numOfRestaurants = 0
avgStarsRestaurants = 0.0
avgNumOfReviews = 0.0
avgNumOfReviewsBus = 0.0

with open(filename, 'r', encoding='UTF-8') as f:
#with open(filename) as f:
    csv_read = csv.reader(f)
    title = next(csv_read)
    for line in csv_read:
        dic = dict(zip(title, line))
        if dic["city"].lower() == city.lower():
            numOfBus += 1
            avgStars += float(dic["stars"])
            avgNumOfReviews += float(dic["review_count"])
            if res(dic["categories"]):
                numOfRestaurants += 1
                avgStarsRestaurants += float(dic["stars"])
                avgNumOfReviewsBus += float(dic["review_count"])
            
print("numOfBus:%d" % (numOfBus) )

avgStars = avgStars / numOfBus
print("avgStars:%.2f" % (avgStars) )

print("numOfRestaurants:%d" % (numOfRestaurants) )

avgStarsRestaurants = avgStarsRestaurants / numOfRestaurants
print("avgStarsRestaurants:%.2f" % (avgStarsRestaurants) )

avgNumOfReviews = avgNumOfReviews / numOfBus
print("avgNumOfReviews:%.2f" % (avgNumOfReviews) )

avgNumOfReviewsBus = avgNumOfReviewsBus / numOfRestaurants
print("avgNumOfReviewsBus:%.2f" % (avgNumOfReviewsBus) )
