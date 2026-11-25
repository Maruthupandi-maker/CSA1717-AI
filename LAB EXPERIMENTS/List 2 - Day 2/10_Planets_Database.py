# Python equivalent of a simple Planets database
planets = [
    ("Mercury", 0.39, 88), ("Venus", 0.72, 225),
    ("Earth", 1.00, 365), ("Mars", 1.52, 687),
    ("Jupiter", 5.20, 4333), ("Saturn", 9.58, 10759)
]
print("PLANETS DATABASE")
print("Planet     Distance(AU)  Orbital period(days)")
for name, distance, period in planets:
    print(f"{name:<10} {distance:<13} {period}")
print("\\nPlanets closer than Earth:")
for name, distance, period in planets:
    if distance < 1:
        print(name)
