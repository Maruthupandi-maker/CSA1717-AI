"""
Experiment 10: Basic Recommendation System using Collaborative Filtering
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# User-Item Rating Matrix (Rows: Users, Columns: Movies)
ratings = pd.DataFrame({
    "Inception":   [5, 4, 1, 0],
    "Interstellar":[5, 5, 1, 2],
    "Toy Story":   [1, 1, 5, 4],
    "Finding Nemo":[0, 2, 5, 5]
}, index=["User1", "User2", "User3", "User4"])

user_sim = pd.DataFrame(
    cosine_similarity(ratings),
    index=ratings.index,
    columns=ratings.index
)

print("=== Collaborative Filtering Recommendation System ===")
print("User-User Cosine Similarity Matrix:")
print(user_sim.round(3))

# Recommend unrated movie for User1 (Finding Nemo = 0) based on most similar user (User2)
similar_user = user_sim["User1"].drop("User1").idxmax()
print(f"\nMost Similar User to User1 : {similar_user}")
print(f"Recommended Movie for User1: Finding Nemo (Rated {ratings.loc[similar_user, 'Finding Nemo']}/5 by {similar_user})")
