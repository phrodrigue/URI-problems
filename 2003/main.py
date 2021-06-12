saida = "Atraso maximo: {}"
while True:
  try:
    H, M = [int(x) for x in input().split(":")]
  except EOFError:
    break

  # M += 60 # maximo de atraso
  # if M >= 60:
  #   M -= 60
  #   H += 1

  # atH = H - 8
  # atM = 0
  # if atH >= 0:
  #   atM = M
  #   while atH > 0:
  #     atM += 60
  #     atH -= 1

  # print(saida.format(atM))

  hora = 8 * 60
  while H > 0:
    M += 60
    H -= 1

  M += 60 # maximo de atraso
  
  atraso = 0 if hora > M else M - hora
  print(saida.format(atraso))


