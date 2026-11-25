# Greedy Best First Search using a priority queue
import heapq

graph = {
    "A": [("B", 1), ("C", 1)],
    "B": [("D", 1), ("E", 1)],
    "C": [("F", 1)],
    "D": [], "E": [("G", 1)], "F": [("G", 1)], "G": []
}
heuristic = {"A": 6, "B": 4, "C": 3, "D": 5, "E": 2, "F": 1, "G": 0}

def best_first_search(start, goal):
    frontier = [(heuristic[start], start, [start])]
    visited = set()
    while frontier:
        _, node, path = heapq.heappop(frontier)
        if node in visited:
            continue
        print("Expanded:", node)
        visited.add(node)
        if node == goal:
            return path
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor, path + [neighbor]))
    return None

print("BEST FIRST SEARCH")
path = best_first_search("A", "G")
print("Path found:", " -> ".join(path) if path else "No path")
