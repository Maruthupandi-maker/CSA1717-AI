"""
Experiment 05: Decision Tree Algorithm for a Simple Classification Problem
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

from sklearn.tree import DecisionTreeClassifier, export_text

# Features: [Weather (0=Sunny,1=Overcast,2=Rain), Temp (0=Hot,1=Mild,2=Cool)]
X = [
    [0, 0], [0, 1], [1, 0], [2, 1],
    [2, 2], [1, 2], [0, 2], [2, 1]
]
# Target: Play Tennis (0=No, 1=Yes)
y = [0, 0, 1, 1, 1, 1, 1, 0]

clf = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)
clf.fit(X, y)

print("=== Decision Tree Classification Rules ===")
print(export_text(clf, feature_names=["Weather", "Temperature"]))
pred = clf.predict([[1, 1]])[0]
print(f"Prediction for [Overcast, Mild]: {'Yes' if pred == 1 else 'No'}")
