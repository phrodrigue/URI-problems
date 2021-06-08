L = int(input())
op = input()
M = []

for m in range(12):
  linha = []
  for i in range(12):
    x = float(input())
    linha.append(x)
  M.append(linha)

if op == "S":
  print(f"{sum(M[L]):0.1f}")
else:
  print(f"{sum(M[L]) / len(M[L]):0.1f}")