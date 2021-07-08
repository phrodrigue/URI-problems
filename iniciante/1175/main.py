v = []
for _ in range(20):
  v.append(int(input()))

for n, i in enumerate(v[::-1]):
  print(f"N[{n}] = {i}")