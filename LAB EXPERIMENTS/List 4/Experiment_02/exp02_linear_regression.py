"""
Experiment 02: Basic Linear Regression Algorithm for Predicting a Continuous Variable
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Study Hours (X) vs Exam Score (y)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([42, 48, 55, 61, 68, 74, 81, 88])

model = LinearRegression()
model.fit(X, y)

test_hours = np.array([[5.5], [9.0]])
predictions = model.predict(test_hours)

print("=== Linear Regression Prediction ===")
print(f"Slope (Weight)    : {model.coef_[0]:.4f}")
print(f"Intercept (Bias)  : {model.intercept_:.4f}")
for hrs, pred in zip(test_hours.flatten(), predictions):
    print(f"Study Hours: {hrs:.1f} -> Predicted Score: {pred:.2f}")
