# Towers of Hanoi using recursion
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)

disks = 3
print("TOWERS OF HANOI")
print(f"Number of disks: {disks}")
hanoi(disks, "A", "B", "C")
