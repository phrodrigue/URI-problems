from math import pow, sqrt

n = int(input())
raizDe5 = sqrt(5)

fib = (pow((1 + raizDe5) / 2, n) - pow((1 - raizDe5) / 2, n)) / raizDe5
print(f"{fib:0.1f}")
