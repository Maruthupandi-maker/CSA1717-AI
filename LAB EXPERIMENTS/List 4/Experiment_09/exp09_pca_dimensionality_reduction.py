"""
Experiment 09: Dimensionality Reduction using Principal Component Analysis (PCA)
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X_scaled = StandardScaler().fit_transform(iris.data)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("=== Principal Component Analysis (PCA) ===")
print(f"Original Feature Shape : {X_scaled.shape}")
print(f"Reduced Feature Shape  : {X_pca.shape}")
print(f"Explained Variance     : {pca.explained_variance_ratio_}")
print(f"Total Variance Retained: {sum(pca.explained_variance_ratio_) * 100:.2f}%")
