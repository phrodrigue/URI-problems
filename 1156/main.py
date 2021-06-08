S = c = 1

for n in range(3, 40, 2):
  c *= 2
  S += (n / c)

print(f"{S:0.2f}")