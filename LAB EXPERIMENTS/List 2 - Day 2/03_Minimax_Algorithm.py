# Minimax algorithm for a small game tree
tree = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"]}
scores = {"D": 3, "E": 5, "F": 2, "G": 9}

def minimax(node, maximizing):
    if node in scores:
        return scores[node]
    values = [minimax(child, not maximizing) for child in tree[node]]
    return max(values) if maximizing else min(values)

print("MINIMAX ALGORITHM")
print("Leaf utility values:", scores)
print("Root A is MAX; next level is MIN.")
print("Best achievable value:", minimax("A", True))
