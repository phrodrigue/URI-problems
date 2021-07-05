while True:
  n = int(input())

  if not n:
    break

  lista = [int(x) for x in input().split()]
  maior = menor = 0

  for i in range(n):
    soma = lista[i] + lista[(i + 1) * -1]

    if soma > maior:
      maior = soma

    if soma < menor or not menor:
      menor = soma

  print(maior, menor)