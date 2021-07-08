saida = ""
while True:
  n = int(input())
  if n == 0:
    break
  
  M = []

  for L in range(1, n+1):
    linha = []
    for C in range(1, n+1):
      valor = L - C + 1
      linha.append(valor)
      if len(linha) == L:
        break
    M.append(linha)

  """
  [1]
  [2, 1]
  [3, 2, 1]
  [4, 3, 2, 1]
  """

  for L in M:
    for c in range(2, n + 1):
      if len(L) == n:
        break
      L.append(c)

  """
  [1, 2, 3, 4]
  [2, 1, 2, 3]
  [3, 2, 1, 2]
  [4, 3, 2, 1]
  """

  for l in M:
    linha = ""
    for item in l:
      linha += f"{item:3} "

    saida += linha[:-1] + "\n"
  saida += "\n"

print(saida[:-1])