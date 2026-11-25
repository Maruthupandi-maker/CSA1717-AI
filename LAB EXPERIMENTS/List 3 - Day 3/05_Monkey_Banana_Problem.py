# Monkey and Banana problem using simple state-space search (BFS)
from collections import deque

# State: (monkey_position, box_position, has_banana)
start = ("door", "window", False)
goal = ("middle", "middle", True)

actions = {
    ("door", "window", False): [
        ("Walk to middle", ("middle", "window", False)),
    ],
    ("middle", "window", False): [
        ("Push box to middle", ("middle", "middle", False)),
        ("Walk to door", ("door", "window", False)),
    ],
    ("middle", "middle", False): [
        ("Climb box and grasp banana", ("middle", "middle", True)),
    ]
}

queue = deque([(start, [])])
visited = {start}
solution = None
while queue:
    state, path = queue.popleft()
    if state == goal:
        solution = path
        break
    for action, next_state in actions.get(state, []):
        if next_state not in visited:
            visited.add(next_state)
            queue.append((next_state, path + [action]))

print("MONKEY AND BANANA PROBLEM")
if solution:
    for step, action in enumerate(solution, 1):
        print(f"Step {step}: {action}")
    print("Goal reached: Monkey gets the banana.")
else:
    print("No solution found.")
