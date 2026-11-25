"""
Experiment 03: K-Nearest Neighbors (KNN) Algorithm for Classification
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.25, random_state=42
)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print("=== K-Nearest Neighbors (KNN, k=5) Classification ===")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
sample = [[5.1, 3.5, 1.4, 0.2]]
pred_class = iris.target_names[knn.predict(sample)[0]]
print(f"Sample {sample[0]} Predicted Class: {pred_class}")
