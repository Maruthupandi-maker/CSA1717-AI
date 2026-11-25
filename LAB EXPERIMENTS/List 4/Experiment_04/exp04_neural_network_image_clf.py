"""
Experiment 04: Neural Network for Image Classification (Digits Dataset)
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

digits = load_digits()
scaler = StandardScaler()
X = scaler.fit_transform(digits.data)
y = digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_t = torch.tensor(X_train, dtype=torch.float32)
y_train_t = torch.tensor(y_train, dtype=torch.long)
X_test_t = torch.tensor(X_test, dtype=torch.float32)
y_test_t = torch.tensor(y_test, dtype=torch.long)

torch.manual_seed(42)
model = nn.Sequential(
    nn.Linear(64, 32),
    nn.ReLU(),
    nn.Linear(32, 10)
)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(50):
    optimizer.zero_grad()
    loss = criterion(model(X_train_t), y_train_t)
    loss.backward()
    optimizer.step()

with torch.no_grad():
    preds = torch.argmax(model(X_test_t), dim=1)
    acc = (preds == y_test_t).float().mean().item() * 100

print("=== PyTorch Neural Network Image Classification ===")
print("Input Image Shape : 8x8 (64 flattened pixels)")
print(f"Final Train Loss  : {loss.item():.4f}")
print(f"Test Set Accuracy : {acc:.2f}%")
