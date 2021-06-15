from math import log

n = int(input())
P = f"{n / log(n):0.1f}"
M = f"{1.25506 * n / log(n):0.1f}"
print(P, M)