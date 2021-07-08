saida = ""
while True:
  try:
    h, m = [int(x) for x in input().split()]
  except EOFError:
    break

  hora = h / (360 / 12)
  min = m / (360 / 60)

  saida += f"{hora:0>2.0f}:{min:0>2.0f}\n"

print(saida[:-1])