# Backward chaining: prove a goal by checking rules and facts
facts = {"fever", "cough"}
rules = {
    "possible_infection": [["fever", "cough"]],
    "recommend_medical_checkup": [["possible_infection"]],
    "monitor_temperature": [["fever"]]
}

def prove(goal, trail=None):
    if trail is None:
        trail = set()
    if goal in facts:
        print(f"Fact found: {goal}")
        return True
    if goal in trail or goal not in rules:
        return False
    trail = trail | {goal}
    for conditions in rules[goal]:
        print(f"To prove {goal}, check {conditions}")
        if all(prove(item, trail) for item in conditions):
            print(f"Goal proved: {goal}")
            return True
    return False

print("BACKWARD CHAINING")
goal = "recommend_medical_checkup"
print("Goal:", goal)
print("Result:", "TRUE" if prove(goal) else "FALSE")
