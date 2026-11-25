"""
Experiment 05: Basic Markov Chain Model for Predicting Sequences of Events
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import numpy as np

states = ["Sunny", "Cloudy", "Rainy"]
# Transition probability matrix
transition_matrix = np.array([
    [0.7, 0.2, 0.1],  # From Sunny
    [0.3, 0.4, 0.3],  # From Cloudy
    [0.2, 0.3, 0.5]   # From Rainy
])

np.random.seed(42)
current_state = 0  # Start with Sunny
sequence = [states[current_state]]

for _ in range(7):
    current_state = np.random.choice([0, 1, 2], p=transition_matrix[current_state])
    sequence.append(states[current_state])

print("=== Markov Chain Weather Prediction ===")
print("Initial State: Sunny")
print("7-Day Forecast Sequence:")
print(" -> ".join(sequence))
