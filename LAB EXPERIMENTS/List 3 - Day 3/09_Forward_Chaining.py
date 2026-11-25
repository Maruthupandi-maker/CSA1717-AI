# Forward chaining: derive new facts from known facts and rules
facts = {"fever", "cough"}
rules = [
    ({"fever", "cough"}, "possible_infection"),
    ({"possible_infection"}, "recommend_medical_checkup"),
    ({"fever"}, "monitor_temperature")
]

print("FORWARD CHAINING")
print("Initial facts:", sorted(facts))
changed = True
while changed:
    changed = False
    for conditions, conclusion in rules:
        if conditions.issubset(facts) and conclusion not in facts:
            facts.add(conclusion)
            changed = True
            print(f"Rule fired: {sorted(conditions)} -> {conclusion}")
print("Final knowledge base:", sorted(facts))
