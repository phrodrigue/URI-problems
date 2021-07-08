while True:
  x = int(input())
  soma = []

  if x == 0:
    break

  while len(soma) < 5:
    if x % 2 == 0:
      soma.append(x)
    x += 1

  print(sum(soma))