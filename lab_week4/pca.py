#!/usr/bin/env python3

​
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA 
​
df = pd.read_csv(sys.argv[1], index_col = "t_name")
df = df.drop(columns = "gene_name")
col_names = df.columns.values.tolist()
​
n, p = df.shape
​
fit = PCA().fit_transform(df.T)
​
# print(fit[:, 1])
​
# fig, ax = plt.subplots()
# ax.bar(range(p), fit.explained_variance_ratio_)
# fig.savefig("scree.png")
# plt.close(fig)
​
sexes = []
stages = []
for name in col_names:
    sex, stage = name.split("_")
    if sex == "female":
        sexes.append("red")
    else:
        sexes.append("blue")
​
fig, ax = plt.subplots()
ax.scatter(fit[:, 0], fit[:, 1], c = sexes)
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
fig.savefig("pca.png")
plt.close()