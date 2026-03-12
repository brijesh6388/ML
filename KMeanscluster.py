# KMeanscluster.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample dataset
X = np.array([
    [1, 2], [1.5, 1.8], [5, 8],
    [8, 8], [1, 0.6], [9, 11],
    [8, 2], [10, 2], [9, 3]
])

# Create K-Means model
kmeans = KMeans(n_clusters=3)

# Train model
kmeans.fit(X)

# Cluster labels
labels = kmeans.labels_

# Cluster centers
centers = kmeans.cluster_centers_

# Plot data points
plt.scatter(X[:,0], X[:,1], c=labels, cmap='rainbow')

# Plot cluster centers
plt.scatter(centers[:,0], centers[:,1], color='black', marker='X', s=200)

plt.title("K-Means Clustering")
plt.show()
