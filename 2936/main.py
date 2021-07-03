gramas = [300, 1500, 600, 1000, 150]
tot = 225

for i in range(5):
  tot += int(input()) * gramas[i]

print(tot)