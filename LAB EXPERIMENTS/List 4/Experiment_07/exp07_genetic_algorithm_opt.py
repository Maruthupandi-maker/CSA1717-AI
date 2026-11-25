"""
Experiment 07: Genetic Algorithm for Optimizing a Mathematical Function
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import numpy as np

# Maximize f(x) = -x^2 + 10x + 25 on [0, 10] (Theoretical max = 50 at x = 5)
def fitness(x):
    return -x**2 + 10*x + 25

np.random.seed(42)
population = np.random.uniform(0, 10, size=20)

for gen in range(50):
    scores = fitness(population)
    parents = population[np.argsort(scores)[-6:]]
    next_gen = list(parents)
    while len(next_gen) < 20:
        p1, p2 = np.random.choice(parents, 2, replace=False)
        child = 0.5 * (p1 + p2) + np.random.normal(0, 0.2)
        child = np.clip(child, 0, 10)
        next_gen.append(child)
    population = np.array(next_gen)

best_x = population[np.argmax(fitness(population))]
print("=== Genetic Algorithm Function Optimization ===")
print("Objective Function : f(x) = -x^2 + 10x + 25")
print(f"Optimal x Found    : {best_x:.4f}")
print(f"Maximum f(x) Value : {fitness(best_x):.4f}")
