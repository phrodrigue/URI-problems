n = int(input())
lista = list(map(int, input().split()))

difs = []

if n == 1:
  print(1)
else:
  ant = "-"
  for i in range(n - 1):
    dif = lista[i + 1] - lista[i]
    if dif != ant:
      ant = dif
      difs.append(dif)
  print(len(difs))