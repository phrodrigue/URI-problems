n = int(input())
c = 1
for i in range(1000):
  print(f"N[{i}] = {c - 1}")
  c = 1 if c == n else c + 1