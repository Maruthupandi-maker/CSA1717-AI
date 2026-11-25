# Educational diet suggestion system based on a selected condition
# This is a simple classroom rule-based example, not medical advice.
diet_rules = {
    "diabetes": ["Choose high-fibre foods", "Prefer whole grains", "Limit sugary drinks"],
    "hypertension": ["Choose fruits and vegetables", "Reduce excess salt", "Limit processed foods"],
    "anaemia": ["Include iron-rich foods", "Add vitamin-C-rich fruits", "Ask a clinician about the cause"]
}

print("DIET SUGGESTION SYSTEM")
for disease in ["diabetes", "hypertension", "anaemia"]:
    print(f"\\nCondition: {disease.title()}")
    for suggestion in diet_rules[disease]:
        print("-", suggestion)
print("\\nNote: Follow advice from a qualified healthcare professional.")
