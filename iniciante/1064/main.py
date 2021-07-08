lista = []
for _ in range(6):
  n = float(input())
  if n > 0:
    lista.append(n)

print(f"{len(lista)} valores positivos")
print(f"{sum(lista) / len(lista):0.1f}")