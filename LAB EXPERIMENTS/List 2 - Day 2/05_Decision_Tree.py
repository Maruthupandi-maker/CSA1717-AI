# Decision Tree classification using a small dataset
from sklearn.tree import DecisionTreeClassifier, export_text

# Outlook: 0=Cloudy, 1=Sunny; Play: 0=No, 1=Yes
X = [[0,0], [0,1], [1,0], [1,1], [1,0], [0,1]]
y = [1, 1, 0, 0, 0, 1]
model = DecisionTreeClassifier(random_state=0, max_depth=3)
model.fit(X, y)
prediction = model.predict([[0, 0]])[0]

print("DECISION TREE CLASSIFIER")
print("Training samples:", len(X))
print("Input [Cloudy, Low humidity] ->", "Play" if prediction == 1 else "Do not play")
print("Decision rules:")
print(export_text(model, feature_names=["Outlook", "Humidity"]))
