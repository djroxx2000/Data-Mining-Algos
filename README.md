# Data-Mining-Algos
Written during third year of Bachelor's of Engineering in Information Technology course for Data Mining and Business Intelligence Practical Assignment

---

## 1. Association Rule Mining (Apriori)
Algorithm to generate frequent itemsets of increasing size with a given minimum support count constraint along with association rules for the same with a given minimum confidence constraint. Every iteration generates itemsets with one extra item.
Dataset Used: Shopping transactions to analyze associations between purchase of certain items

## 2. Classification Algorithm (ID3)
Algorithm to classify rows of data based on the unique classes provided in a single target or result column. Iteratively generates nodes for the decision tree by determining column providing maximum information gained on splitting dataset on the column at mean value. Assigns target class to each node for classification and left and right keys to determine which node to check next depending on comparison result.
Dataset Used: Seaborn iris dataset to classify flowers into 3 species classes based on petal length, petal width, sepal length and sepal width.

## 3. Clustering Algorithm (Simple K-means)
Unsupervised algorithm to cluster rows of data into k clusters by starting with k random rows chosen as centroids and populating clusters with rows which have smallest euclidean distance to a centroid then updating centroids to have the mean values of all rows in their cluster.
Dataset Used: Seaborn iris dataset to classify flowers into 3 species classes based on petal length, petal width, sepal length and sepal width.