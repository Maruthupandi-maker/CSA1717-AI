# Simple family tree facts and relationship queries
parent = {
    ("rajan", "arun"), ("rajan", "meena"),
    ("arun", "kavin"), ("meena", "divya")
}

def children_of(person):
    return [child for p, child in sorted(parent) if p == person]

def is_grandparent(grandparent, child):
    return any((grandparent, middle) in parent and (middle, child) in parent
               for middle in {p for p, _ in parent})

print("FAMILY TREE")
for person in ["rajan", "arun", "meena"]:
    print(f"Children of {person.title()}: {', '.join(children_of(person)) or 'None'}")
print("Is Rajan the grandparent of Kavin?", is_grandparent("rajan", "kavin"))
