n = int(input())

nIn = nOut = 0

for _ in range(n):
  i = int(input())

  if 10 <= i <= 20:
    nIn += 1
  else:
    nOut += 1

print(f"{nIn} in\n{nOut} out")