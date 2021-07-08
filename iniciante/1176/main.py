fib = [0, 1]
for i in range(60):
  fib.append(fib[i] + fib[i + 1])

t = int(input())

for i in range(t):
  n = int(input())
  print(f"Fib({n}) = {fib[n]}")