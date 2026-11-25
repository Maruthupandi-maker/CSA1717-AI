"""
Experiment 09: Face Recognition using Pre-Trained Deep Feature Embeddings
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Simulated 128-D normalized FaceNet embeddings
np.random.seed(10)
database = {
    "Maruthu_Pandi": np.random.rand(1, 128),
    "Arun_Kumar": np.random.rand(1, 128),
    "Priya_Sharma": np.random.rand(1, 128)
}

# Probe embedding close to Maruthu_Pandi with slight lighting noise
probe_embedding = database["Maruthu_Pandi"] + np.random.normal(0, 0.05, (1, 128))

print("=== Face Recognition Embedding Matching ===")
best_match = None
highest_sim = -1.0

for name, emb in database.items():
    sim = cosine_similarity(probe_embedding, emb)[0][0]
    print(f"Cosine Similarity with {name:15s}: {sim:.4f}")
    if sim > highest_sim:
        highest_sim = sim
        best_match = name

print(f"\nIdentified Person: {best_match} (Confidence: {highest_sim*100:.2f}%)")
