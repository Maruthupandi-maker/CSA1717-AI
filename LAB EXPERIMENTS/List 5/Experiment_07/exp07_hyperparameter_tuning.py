"""
Experiment 07: Hyperparameter Tuning for a Machine Learning Model using GridSearchCV
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.25, random_state=42
)

param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

grid = GridSearchCV(SVC(), param_grid, cv=5)
grid.fit(X_train, y_train)

print("=== Hyperparameter Tuning (GridSearchCV on SVM) ===")
print("Best Hyperparameters:", grid.best_params_)
print(f"Best Cross-Validation Score: {grid.best_score_ * 100:.2f}%")
print(f"Test Set Accuracy: {grid.score(X_test, y_test) * 100:.2f}%")
