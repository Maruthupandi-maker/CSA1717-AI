# Alpha-Beta pruning on a small game tree
tree = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"]}
scores = {"D": 3, "E": 5, "F": 2, "G": 9}
visited = []

def alphabeta(node, alpha, beta, maximizing):
    if node in scores:
        visited.append(node)
        return scores[node]
    if maximizing:
        value = float("-inf")
        for child in tree[node]:
            value = max(value, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                print("Pruned remaining branches below", node)
                break
        return value
    value = float("inf")
    for child in tree[node]:
        value = min(value, alphabeta(child, alpha, beta, True))
        beta = min(beta, value)
        if beta <= alpha:
            print("Pruned remaining branches below", node)
            break
    return value

print("ALPHA-BETA PRUNING")
best = alphabeta("A", float("-inf"), float("inf"), True)
print("Best value:", best)
print("Evaluated leaf nodes:", visited)
