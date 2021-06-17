while True:
  try:
    n, m = [int(x) for x in input().split()]
  except EOFError:
    break

  M = []
  for _ in range(n):
    M.append([int(x) for x in input().split()])
  
  for l in range(n):
    saida = ""
    # print(M[l])
    for c in range(m):
      print(l, c)
      if M[l][c] == 1:
        saida += "9"
      else:
        lista = [
          M[l - 1][c] if l >= 0 else 0,
          M[l][c + 1] if c < m - 1 else 0,
          M[l + 1][c] if l < n - 1 else 0,
          M[l][c - 1] if c >= 0 else 0,
        ]
        saida += str(sum(lista))
        print(lista)
    print(saida)

