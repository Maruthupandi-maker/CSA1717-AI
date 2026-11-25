"""
Experiment 08: Support Vector Machine (SVM) for Binary Classification
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data = load_breast_cancer()
scaler = StandardScaler()
X = scaler.fit_transform(data.data)
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svm_clf = SVC(kernel="rbf", C=1.0, gamma="scale")
svm_clf.fit(X_train, y_train)
y_pred = svm_clf.predict(X_test)

print("=== Support Vector Machine (SVM) Binary Classification ===")
print(f"Dataset         : Breast Cancer Wisconsin ({len(X)} samples)")
print(f"Kernel          : RBF")
print(f"Test Accuracy   : {accuracy_score(y_test, y_pred) * 100:.2f}%")
