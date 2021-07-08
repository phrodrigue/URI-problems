while True:
  try:
    V = float(input())
    D = float(input())
  except EOFError:
    break

  r = D / 2
  AREA = 3.14 * (r ** 2)
  ALTURA = V / AREA
  print(f"ALTURA = {ALTURA:0.2f}\nAREA = {AREA:0.2f}")