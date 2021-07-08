pares, impares, positivos, negativos = ([] for _ in range(4))

for _ in range(5):
  n = float(input())

  if n % 2 == 0:
    pares.append(n)
  else:
    impares.append(n)

  if n > 0:
    positivos.append(n)
  elif n < 0:
    negativos.append(n)

print(f"{len(pares)} valor(es) par(es)\n{len(impares)} valor(es) impar(es)\n{len(positivos)} valor(es) positivo(s)\n{len(negativos)} valor(es) negativo(s)")