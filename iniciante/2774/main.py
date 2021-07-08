from math import sqrt, pow

while True:
  try:
    h, m = [int(x) for x in input().split()]
  except EOFError:
    break

  leituras = [float(x) for x in input().split()]
  qt = len(leituras)
  media = sum(leituras) / qt

  ac = 0
  for l in leituras:
    ac += pow(l - media, 2)

  res = sqrt(ac / (qt - 1))

  print(f"{res:0.5f}")