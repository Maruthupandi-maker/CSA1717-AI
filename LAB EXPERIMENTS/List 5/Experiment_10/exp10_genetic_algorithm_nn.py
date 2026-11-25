"""
Experiment 10: Genetic Algorithm to Evolve Neural Network Weights for XOR Problem
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import numpy as np

# XOR Dataset
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def evaluate_fitness(chromosome):
    # Architecture: 2 -> 2 -> 1 (9 parameters total)
    W1 = chromosome[:4].reshape(2, 2)
    b1 = chromosome[4:6].reshape(1, 2)
    W2 = chromosome[6:8].reshape(2, 1)
    b2 = chromosome[8:9].reshape(1, 1)
    hidden = sigmoid(np.dot(X, W1) + b1)
    out = sigmoid(np.dot(hidden, W2) + b2)
    mse = np.mean((y - out) ** 2)
    return 1.0 / (mse + 1e-6), out

np.random.seed(42)
pop_size = 60
population = np.random.uniform(-3, 3, (pop_size, 9))

for gen in range(300):
    scores = [evaluate_fitness(ind)[0] for ind in population]
    ranked = [x for _, x in sorted(zip(scores, population), key=lambda pair: pair[0], reverse=True)]
    next_gen = ranked[:10]
    while len(next_gen) < pop_size:
        p1, p2 = ranked[np.random.randint(0, 15)], ranked[np.random.randint(0, 15)]
        cut = np.random.randint(1, 8)
        child = np.concatenate([p1[:cut], p2[cut:]])
        if np.random.rand() < 0.3:
            child[np.random.randint(0, 9)] += np.random.normal(0, 0.5)
        next_gen.append(child)
    population = np.array(next_gen)

best_ind = max(population, key=lambda ind: evaluate_fitness(ind)[0])
_, preds = evaluate_fitness(best_ind)

print("=== Neuroevolution (GA + Neural Network) for XOR ===")
for inp, target, pred in zip(X, y, preds):
    print(f"Input: {inp} | Expected: {target[0]} | Evolved NN Output: {pred[0]:.4f}")
