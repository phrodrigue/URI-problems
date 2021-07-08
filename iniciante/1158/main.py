n = int(input())

for _ in range(n):
  inicio, c = [int(x) for x in input().split()]
  soma = []

  while len(soma) < c:
    if inicio % 2 != 0:
      soma.append(inicio)

    inicio += 1
  
  print(sum(soma))