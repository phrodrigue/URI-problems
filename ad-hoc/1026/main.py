while True:
  try:
    a, b = [int(x) for x in input().split()]
  except EOFError:
    break

  aBin = bin(a)[2:]
  bBin = bin(b)[2:]

  ta = len(aBin)
  tb = len(bBin)

  while ta != tb:
    if ta > tb:
      bBin = "0" + bBin
      tb += 1
    else:
      aBin = "0" + aBin
      ta += 1

  soma = ""
  for i in range(1, len(aBin) + 1):
    i *= -1
    x = aBin[i]
    y = bBin[i]

    if x == y == "0" or x == y == "1":
      v = "0"
    elif x != y:
      v = "1"

    soma = v + soma

  print(int(soma, 2))