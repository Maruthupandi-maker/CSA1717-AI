# Bird flight facts and queries
birds = {
    "eagle": {"can_fly": True, "reason": "It has wings and is a flying bird."},
    "sparrow": {"can_fly": True, "reason": "It is a small flying bird."},
    "penguin": {"can_fly": False, "reason": "Penguins are flightless birds."},
    "ostrich": {"can_fly": False, "reason": "Ostriches are flightless birds."}
}

def can_bird_fly(name):
    bird = birds.get(name.lower())
    if bird is None:
        return "Bird information not available."
    return f"Yes, {name} can fly. {bird['reason']}" if bird["can_fly"] else f"No, {name} cannot fly. {bird['reason']}"

print("BIRD FLIGHT DATABASE")
for query in ["eagle", "penguin", "sparrow"]:
    print(f"Query: Can {query} fly?")
    print(can_bird_fly(query))
