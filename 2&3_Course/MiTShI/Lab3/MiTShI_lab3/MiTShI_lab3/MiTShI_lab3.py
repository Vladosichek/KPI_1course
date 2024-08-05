import numpy as np 
import skfuzzy as fuzz 
import matplotlib.pyplot as plt 
from sklearn.datasets import make_blobs 

n_samples = 700   # Number of data
centers = [[4, 2], [3, 7], [7, 5], [6, 9], [8, 1]]    # Centers of clusters

# Create blobs for clustering 
data, _ = make_blobs(n_samples=n_samples, centers=centers, cluster_std=1.0, random_state=42) 

# Plot data 
plt.scatter(data[:, 0], data[:, 1], s=20) 
plt.title('Data') 
plt.xlabel('Feature 1') 
plt.ylabel('Feature 2') 
plt.show() 

# Parameters for fuzzy cmeans 
cl = 5 # Number of clusters 
m = 3 # Degree of fuzziness 

cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(data.T, cl, m, error=0.005, maxiter=20, init=None) 
fuzzy_labels = np.argmax(u, axis=0) 

# Plot clusters 
for i in range(cl): 
    cluster_points = data[fuzzy_labels == i] 
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i + 1}', s=20) 
plt.scatter(cntr[:, 0], cntr[:, 1], marker='x', s=100, color='black') 
plt.title('Clusters') 
plt.xlabel('Feature 1') 
plt.ylabel('Feature 2') 
plt.legend() 
plt.show() 

#Centers of clusters
print("Centers of clusters:")
for cnt in cntr:
    print(cnt)

# Plot objective function values over iterations 
plt.plot(jm) 
plt.xlabel('Iterations') 
plt.ylabel('Objective function values') 
plt.title('Objective function values over iterations') 
plt.grid(True) 
plt.show()
