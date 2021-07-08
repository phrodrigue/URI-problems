v, n = [int(x) for x in input().split()]
totPlacas = v * n
saida = ""

for i in range(1, 10):
  pl = totPlacas * (i / 10)
  intPL = int(pl)
  placas = intPL + 1 if pl - intPL > 0 else intPL

  saida += f"{placas} "

print(saida[:-1])