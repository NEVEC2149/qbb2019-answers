#!/usr/bin/env python3 

import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy 
import pandas as pd
from pandas import DataFrame
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from sklearn.cluster import KMeans

data = pd.read_csv(sys.argv[1])

cfu = data["CFU"].values
poly = data["poly"].values
int1 = data["int"].values
unk = data["unk"].values 

newdata = {'x':cfu, 'y':poly}
dataframe = DataFrame(newdata,columns = ['x', 'y'])
kmeans = KMeans(n_clusters = 5).fit(dataframe)
centroids = kmeans.cluster_centers_

plt.scatter(dataframe['x'], dataframe['y'], c = kmeans.labels_.astype(float), s = 50)
plt.scatter(centroids[:,0], centroids[:,1])
plt.xlabel("cfu")
plt.ylabel("poly")
plt.savefig("k_means.png")