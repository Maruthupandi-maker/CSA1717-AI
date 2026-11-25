# Basic rule-based medical diagnosis demonstration
# Educational example only; it does not provide a real diagnosis.
rules = [
    ({"fever", "cough"}, "Possible respiratory infection"),
    ({"sneezing", "runny_nose"}, "Possible common cold or allergy"),
    ({"fever", "body_pain"}, "Possible flu-like illness")
]

def diagnose(symptoms):
    matches = [condition for required, condition in rules if required.issubset(symptoms)]
    return matches or ["No matching rule. Consult a healthcare professional."]

print("RULE-BASED MEDICAL DIAGNOSIS (DEMO)")
case_symptoms = {"fever", "cough"}
print("Observed symptoms:", ", ".join(sorted(case_symptoms)))
print("System output:")
for result in diagnose(case_symptoms):
    print("-", result)
print("Note: This program is for learning purposes, not medical advice.")
