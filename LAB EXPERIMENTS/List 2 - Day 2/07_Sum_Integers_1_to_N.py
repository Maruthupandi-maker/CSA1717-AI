# Python equivalent of the Prolog task: sum integers from 1 to N
def sum_to_n(n):
    if n <= 0:
        return 0
    return n + sum_to_n(n - 1)

n = 5
print("SUM OF INTEGERS FROM 1 TO N")
print(f"N = {n}")
print(f"Sum = {sum_to_n(n)}")
