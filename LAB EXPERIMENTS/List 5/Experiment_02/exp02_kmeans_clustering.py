"""
Experiment 02: K-Means Clustering Algorithm for Grouping Similar Data Points
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import numpy as np
from sklearn.cluster import KMeans

# Sample 2D dataset
X = np.array([
    [1.0, 2.0], [1.5, 1.8], [1.2, 2.2],
    [5.0, 8.0], [6.0, 9.0], [5.5, 8.5],
    [9.0, 1.0], [8.5, 1.5], [9.2, 0.8]
])

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

print("=== K-Means Clustering Results ===")
print("Cluster Centroids:")
for i, center in enumerate(kmeans.cluster_centers_):
    print(f"  Cluster {i}: ({center[0]:.2f}, {center[1]:.2f})")

print("\nData Point Assignments:")
for point, label in zip(X, kmeans.labels_):
    print(f"  Point {point} -> Cluster {label}")
