# Assign fruit colors using backtracking
fruits = ["Apple", "Banana", "Grapes"]
colors = ["Red", "Yellow", "Green", "Purple"]
assignment = {}

# Example constraints: each fruit receives one allowed color.
allowed = {
    "Apple": ["Red", "Green"],
    "Banana": ["Yellow"],
    "Grapes": ["Green", "Purple"]
}

def backtrack(index):
    if index == len(fruits):
        return True
    fruit = fruits[index]
    for color in allowed[fruit]:
        if color not in assignment.values():
            assignment[fruit] = color
            if backtrack(index + 1):
                return True
            del assignment[fruit]
    return False

print("FRUIT COLOR ASSIGNMENT USING BACKTRACKING")
if backtrack(0):
    for fruit, color in assignment.items():
        print(f"{fruit} -> {color}")
else:
    print("No valid assignment found.")
