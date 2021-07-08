while True:
  try:
    n, d = [int(x) for x in input().split()]
  except EOFError:
    break

  saida = "Pizza antes de FdI"
  for _ in range(d):
    entrada = input().split()
    p = [int(x) for x in entrada[1:]]
    if sum(p) == n and saida == "Pizza antes de FdI":
      saida = entrada[0]
  print(saida)