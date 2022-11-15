#This project provide some data analytics on Yelp businesses and its network.
<br>
##1. dstats
<br>
It given a collection of businesses in a file filename.csv.
And a name of a city city computes and prints out (in the STDOUT) the following statistics:
<br>• **numOfBus**: the number of businesses in the city
<br>• **avgStars**: the average number of stars of a business in the city
<br>• **numOfRestaurants**: the number of restaurants in the city
<br>• **avgStarsRestaurants**: the average number of stars of restaurants in the city
<br>• **avgNumOfReviews**: the average number of reviews for all businesses in the city
<br>• **avgNumOfReviewsBus**: the average number of reviews for restaurants in the city

##2. dist-stats
<br>
This can show the following:
**restaurantCategoryDist**: a frequency distribution of the number of restaurants in each category of restaurants (e.g., Chinese, Japanese, Korean, Greek, etc.) in a descending order of popularity (from the most popular category to the least popular) <br>
**restaurantReviewDist**: a frequency distribution of the number of reviews submitted for each category of restaurants (e.g., Chinese, Japanese, Korean, Greek, etc.) in a descending order (from the most reviewed category to the least reviewed), along with the average number of stars received per category. <br>
**create a bar chart** that shows the top-10 of restaurantCategoryDist found earlier, where the x-axis represents the restaurant category and the y-axis represents its frequency (#restaurants).

##3. yelp-network
<br>
It given a collection of users in a file filename.csv creates a file yelp-network.txt that represents the social network of Yelp friends. The social network will be represented as a graph G(V,E), where V is a set of vertices/nodes representing the Yelp users and E is a set of links/edges representing friendships between Yelp users. The graph/network should be represented in a file using the edge list format. An edge list is a list that represents all the edges in a graph. Each edge is represented as a pair of nodes occupying a new line in the file.

##4. graph-stats
<br>
It prints the following with given a file of network as input:
**the number of nodes (|N|) and edges (|E|) of the network**
**nodeDegreeDist**: a frequency distribution of the node degrees of the network, in a descending order of frequency (from the highest to the lowest frequency). The degree of a node is the number of edges that are incident to the node (i.e., #neighbors). 
