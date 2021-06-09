C = int(input())
op = input()
M = []
lista = []

for m in range(12):
  linha = []
  for i in range(12):
    x = float(input())
    linha.append(x)
    if i == C:
      lista.append(x)
  M.append(linha)


if op == "S":
  print(f"{sum(lista):0.1f}")
else:
  print(f"{sum(lista) / len(lista):0.1f}")