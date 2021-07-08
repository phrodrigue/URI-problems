n = int(input())

for i in range(n):
  atl = input()
  gd = float(input())
  notas = list(map(float, input().split()))
  notas.pop(notas.index(min(notas)))
  notas.pop(notas.index(max(notas)))
  res = sum(notas) * gd
  print(f"{atl} {res:0.2f}")