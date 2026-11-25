# Map Coloring using Constraint Satisfaction Problem (CSP)
regions = ["A", "B", "C", "D"]
neighbors = {"A": ["B", "C"], "B": ["A", "C", "D"],
             "C": ["A", "B", "D"], "D": ["B", "C"]}
colors = ["Red", "Green", "Blue"]
assignment = {}

def consistent(region, color):
    return all(assignment.get(n) != color for n in neighbors[region])

def solve():
    if len(assignment) == len(regions):
        return True
    region = next(r for r in regions if r not in assignment)
    for color in colors:
        if consistent(region, color):
            assignment[region] = color
            if solve():
                return True
            del assignment[region]
    return False

print("MAP COLORING USING CSP")
if solve():
    for region in regions:
        print(f"Region {region} -> {assignment[region]}")
    print("Constraint check: No adjacent regions have the same color.")
else:
    print("No solution found.")
