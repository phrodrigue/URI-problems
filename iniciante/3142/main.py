alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
  try:
    S = input()
  except EOFError:
    break

  t = len(S)

  if t <= 3:
    soma = 0
    if t == 1:
      c = alfabeto.index(S) + 1
      soma = c
    elif t == 2:
      b = alfabeto.index(S[0]) + 1
      c = alfabeto.index(S[1]) + 1
      soma = (b * 26) + c
    else:
      a = alfabeto.index(S[0])
      b = alfabeto.index(S[1])
      c = alfabeto.index(S[2])
      soma = ((a * 676) + 702) + (b * 26) + (c + 1)
  
    saida = soma if soma <= 16384 else "Essa coluna nao existe Tobias!"

  else:
    saida = "Essa coluna nao existe Tobias!"

  print(saida)
