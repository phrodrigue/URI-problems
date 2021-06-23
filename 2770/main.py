while True:
  try:
    x, y, n = [int(x) for x in input().split()]
  except EOFError:
    break

  xy = [x, y]
  xy.sort()
  for _ in range(n):
    xyi = [int(x) for x in input().split()]
    menor = xyi[0] if xyi[0] < xyi[1] else xyi[1]
    maior = xyi[0] if xyi[0] > xyi[1] else xyi[1]
    if xy[0] >= menor and xy[1] >= maior:
      print("Sim")
    else:
      print("Nao")