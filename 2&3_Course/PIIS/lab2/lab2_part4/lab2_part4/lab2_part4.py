import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import AffinityPropagation
from sklearn.metrics.cluster import adjusted_rand_score
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics import silhouette_score


mall_data = pd.read_csv("Mall_Customers.csv")
X_numerics = mall_data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

#KMeans
KM_6_clusters = KMeans(n_clusters=6, init='k-means++').fit(X_numerics) 
KM6_clustered = X_numerics.copy()
KM6_clustered.loc[:,'Cluster'] = KM_6_clusters.labels_
fig1, axes = plt.subplots(1,2,figsize=(12,5))
scat_1 = sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=KM6_clustered,
                hue='Cluster', ax=axes[0], palette='Set1', legend='full')
scat2=sns.scatterplot(x='Age', y='Spending Score (1-100)', data=KM6_clustered,
                hue='Cluster', palette='Set1', ax=axes[1], legend='full')
axes[0].scatter(KM_6_clusters.cluster_centers_[:,1],KM_6_clusters.cluster_centers_[:,2], marker='s', s=40, c="blue")
axes[1].scatter(KM_6_clusters.cluster_centers_[:,0],KM_6_clusters.cluster_centers_[:,2], marker='s', s=40, c="blue")
plt.show()

#AP
AP = AffinityPropagation(preference=-11800).fit(X_numerics)
AP_clustered = X_numerics.copy()
AP_clustered.loc[:,'Cluster'] = AP.labels_ 
fig3, (ax_af) = plt.subplots(1,2,figsize=(12,5))
scat_1 = sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', data=AP_clustered,
                hue='Cluster', ax=ax_af[0], palette='Set1', legend='full')
sns.scatterplot(x='Age', y='Spending Score (1-100)', data=AP_clustered,
                hue='Cluster', palette='Set1', ax=ax_af[1], legend='full')
plt.setp(ax_af[0].get_legend().get_texts(), fontsize='10')
plt.setp(ax_af[1].get_legend().get_texts(), fontsize='10')
plt.show()

#Metrics
KM_sizes=KM6_clustered.groupby('Cluster').size().to_frame()
KM_sizes.columns=["K-Means Cluster Size"]
AP_sizes=AP_clustered.groupby('Cluster').size().to_frame()
AP_sizes.columns=["AF Cluster Size"]
clusters=pd.concat([KM_sizes,AP_sizes],axis=1, sort=False)
print(clusters)

print("K-Means Silhouette =",silhouette_score(X_numerics, KM_6_clusters.labels_))
print("AP Silhouette =",silhouette_score(X_numerics, AP.labels_))
print("ARI =", adjusted_rand_score(KM_6_clusters.labels_, AP.labels_))
print("NMI =", normalized_mutual_info_score(KM_6_clusters.labels_, AP.labels_))
