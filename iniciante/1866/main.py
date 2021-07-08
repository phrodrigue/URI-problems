n = int(input())

for _ in range(n):
  c = int(input())
  s = 0
  for q in range(c):
    s += 1 if q % 2 == 0 else - 1
  print(s)