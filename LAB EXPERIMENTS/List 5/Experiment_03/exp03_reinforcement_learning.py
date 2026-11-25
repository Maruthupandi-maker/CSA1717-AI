"""
Experiment 03: Reinforcement Learning Agent (Q-Learning) for a Grid Environment
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import numpy as np
import random

# 1D Grid Environment: States 0 to 4 (State 4 is Goal)
n_states = 5
actions = [0, 1]  # 0: Left, 1: Right
Q = np.zeros((n_states, len(actions)))

alpha = 0.1      # Learning rate
gamma = 0.9      # Discount factor
epsilon = 0.2    # Exploration rate
episodes = 200

for ep in range(episodes):
    state = 0
    while state != 4:
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)
        else:
            action = np.argmax(Q[state])

        next_state = max(0, state - 1) if action == 0 else min(4, state + 1)
        reward = 10 if next_state == 4 else -1

        Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
        state = next_state

print("=== Trained Q-Table (Left vs Right) ===")
for s in range(n_states):
    print(f"State {s}: Left={Q[s,0]:.2f}, Right={Q[s,1]:.2f}")

# Test optimal policy
state = 0
path = [state]
while state != 4:
    action = np.argmax(Q[state])
    state = max(0, state - 1) if action == 0 else min(4, state + 1)
    path.append(state)
print(f"\nOptimal Path to Goal: {' -> '.join(map(str, path))}")
