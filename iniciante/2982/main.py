n = int(input())
g = v = 0

for _ in range(n):
  t, c = input().split()

  if t == "G":
    g += int(c)
  else:
    v += int(c)

print("NAO VAI TER CORTE, VAI TER LUTA!" if v < g else "A greve vai parar.")