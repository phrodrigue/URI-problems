while True:
  n = int(input())
  if n == 0:
    break
  for _ in range(n):
    c = int(input())
    pontas = 2 if c % 2 == 0 else 1
    saida = (c - pontas) * 2 + pontas
    print(saida)
