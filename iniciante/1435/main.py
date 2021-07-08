saida = ""
while True:
  n = int(input())
  if n == 0:
    break
  
  M = []

  metade = int(n / 2) + 1 if n % 2 != 0 else int(n / 2)
  for L in range(1, metade + 1):
    linha = []
    for C in range(1, metade + 1):
      valor = C
      linha.append(valor)
      if len(linha) == L:
        break
    M.append(linha)
  
  """
  [1]
  [1, 2]
  [1, 2, 3]
  """

  for L in range(0, metade):
    for C in range(0, metade):
      while len(M[L]) < metade:
        M[L].append(L + 1)

  """
  [1, 1, 1]
  [1, 2, 2]
  [1, 2, 3]
  """

  c = metade - 1 if n % 2 != 0 else metade
  while len(M) < n:
    M.append(M[c - 1][:])
    c -= 1

  """
  [1, 1, 1]
  [1, 2, 2]
  [1, 2, 3]
  [1, 2, 2]
  [1, 1, 1]
  """

  c = metade - 1 if n % 2 != 0 else metade
  for L in M:
    for i in range(c - 1, -1, -1):
      L.append(L[i])

  """
  [1, 1, 1, 1, 1]
  [1, 2, 2, 2, 1]
  [1, 2, 3, 2, 1]
  [1, 2, 2, 2, 1]
  [1, 1, 1, 1, 1]
  """

  for l in M:
    linha = ""
    for item in l:
      linha += f"{item:3} "

    saida += linha[:-1] + "\n"
  saida += "\n"

print(saida[:-1])