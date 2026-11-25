# Feed Forward Neural Network using scikit-learn
from sklearn.neural_network import MLPClassifier

X = [[0,0], [0,1], [1,0], [1,1]]
y = [0, 1, 1, 0]  # XOR
model = MLPClassifier(hidden_layer_sizes=(4,), activation="tanh",
                      solver="lbfgs", max_iter=5000, random_state=1)
model.fit(X, y)

print("FEED FORWARD NEURAL NETWORK")
print("XOR truth table predictions:")
for row in X:
    print(f"{row[0]} XOR {row[1]} = {model.predict([row])[0]}")
