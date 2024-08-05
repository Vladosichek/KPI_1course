import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import Birch, AgglomerativeClustering, DBSCAN
from sklearn import datasets
from sklearn.datasets import make_blobs
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics import silhouette_score
import pandas as pd

np.random.seed(10)

#Datasets
X1,Y1 = datasets.make_moons(n_samples=2000, noise=.09,random_state=10)
X2,Y2  = make_blobs(n_samples=2000,cluster_std=3.5,centers=2, n_features=2,random_state=10)
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.scatter(X1[:, 0], X1[:, 1], s=10, c=Y1)
plt.title('Dataset 1')
plt.subplot(1,2,2)
plt.scatter(X2[:, 0], X2[:, 1], s=10, c=Y2)
plt.title('Dataset 2')
plt.show()

#Agnes
agnesmodel = AgglomerativeClustering(n_clusters=2)
y_agnes=agnesmodel.fit_predict(X1)
agnesmodel2 = AgglomerativeClustering(n_clusters=2)
y_agnes2=agnesmodel2.fit_predict(X2)
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.scatter(X1[:, 0], X1[:, 1], s=10, c=y_agnes)
plt.title('Agnes Dataset1')
plt.subplot(1,2,2)
plt.scatter(X2[:, 0], X2[:, 1], s=10, c=y_agnes2)
plt.title('Agnes Dataset2')
plt.show()

#Birch
birchmodel=Birch(n_clusters=2,threshold=0.5,branching_factor=100)
y_birch=birchmodel.fit_predict(X1)
birchmodel2=Birch(n_clusters=2,threshold=0.1,branching_factor=100)
y_birch2=birchmodel2.fit_predict(X2)
plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.scatter(X1[:, 0], X1[:, 1], s=10, c=y_birch)
plt.title('Birch Dataset1')
plt.subplot(1,2,2)
plt.scatter(X2[:, 0], X2[:, 1], s=10, c=y_birch2)
plt.title('Birch Dataset2')
plt.show()

#DBSCAN
dbscanmodel=DBSCAN(eps=.2, min_samples=70)
y_dbscan=dbscanmodel.fit_predict(X1)
dbscanmodel2=DBSCAN(eps=1,min_samples=10)
y_dbscan2=dbscanmodel2.fit_predict(X2)
plt.figure(figsize=(14,5))
plt.subplot(1,2,1)
plt.scatter(X1[:, 0], X1[:, 1], s=10, c=y_dbscan)
plt.title('DBSCAN Dataset1')
plt.subplot(1,2,2)
plt.scatter(X2[:, 0], X2[:, 1], s=10, c=y_dbscan2)
plt.title('DBSCAN Dataset2')
plt.show()

# Metrics
data1 = {
    'Model': ['Agnes', 'Birch', 'DBSCAN'],
    'Silhouette Coefficient': [
        silhouette_score(X1, y_agnes),
        silhouette_score(X1, y_birch),
        silhouette_score(X1, y_dbscan)
    ],
    'ARI': [
        adjusted_rand_score(Y1, y_agnes),
        adjusted_rand_score(Y1, y_birch),
        adjusted_rand_score(Y1, y_dbscan)
    ],
    'NMI': [
        normalized_mutual_info_score(Y1, y_agnes),
        normalized_mutual_info_score(Y1, y_birch),
        normalized_mutual_info_score(Y1, y_dbscan)
    ]
}
data2 = {
    'Model': ['Agnes', 'Birch', 'DBSCAN'],
    'Silhouette Coefficient': [
        silhouette_score(X2, y_agnes2),
        silhouette_score(X2, y_birch2),
        silhouette_score(X2, y_dbscan2)
    ],
    'ARI': [
        adjusted_rand_score(Y2, y_agnes2),
        adjusted_rand_score(Y2, y_birch2),
        adjusted_rand_score(Y2, y_dbscan2)
    ],
    'NMI': [
        normalized_mutual_info_score(Y2, y_agnes2),
        normalized_mutual_info_score(Y2, y_birch2),
        normalized_mutual_info_score(Y2, y_dbscan2)
    ]
}
print('Dataset 1\n', pd.DataFrame(data1).set_index('Model').T, sep='', end='\n\n')
print('Dataset 2\n', pd.DataFrame(data2).set_index('Model').T, sep='')