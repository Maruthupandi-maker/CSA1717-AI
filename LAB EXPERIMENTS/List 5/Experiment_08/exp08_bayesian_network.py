"""
Experiment 08: Bayesian Network for Modeling Probabilistic Relationships
Name   : S. Maruthu Pandi
Reg No : 192511162
Course : CSA1717 - Artificial Intelligence
College: Saveetha School of Engineering
"""

# Bayesian Network: Rain -> Sprinkler -> WetGrass
P_Rain = {True: 0.2, False: 0.8}
P_Sprinkler_given_Rain = {
    True: {True: 0.01, False: 0.99},
    False: {True: 0.40, False: 0.60}
}
P_WetGrass_given_SR = {
    (True, True): 0.99,
    (True, False): 0.80,
    (False, True): 0.90,
    (False, False): 0.00
}

# Compute joint probability and posterior P(Rain=True | WetGrass=True)
joint_true = 0.0
joint_false = 0.0

for s in [True, False]:
    # Rain = True
    p_t = P_Rain[True] * P_Sprinkler_given_Rain[True][s] * P_WetGrass_given_SR[(s, True)]
    joint_true += p_t
    # Rain = False
    p_f = P_Rain[False] * P_Sprinkler_given_Rain[False][s] * P_WetGrass_given_SR[(s, True)]
    joint_false += p_f

p_wet = joint_true + joint_false
p_rain_given_wet = joint_true / p_wet

print("=== Bayesian Network Probabilistic Inference ===")
print(f"Prior P(Rain = True)              : {P_Rain[True]:.4f}")
print(f"Marginal P(WetGrass = True)       : {p_wet:.4f}")
print(f"Posterior P(Rain=True | WetGrass) : {p_rain_given_wet:.4f} ({p_rain_given_wet*100:.2f}%)")
