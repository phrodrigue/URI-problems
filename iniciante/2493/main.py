while True:
  try:
    n = int(input())
  except EOFError:
    break
  expr = []
  perdeu = []
  for _ in range(n):
    X, YZ = input().split()
    Y, Z = YZ.split("=")
    l = list(map(int, [X, Y, Z]))
    expr.append(l)
  
  for _ in range(n):
    jogador, expressao, op = input().split()
    exprSelec = expr[int(expressao) - 1]

    if op == "I":
      # testes pra ver se é impossivel
      resSoma = exprSelec[0] + exprSelec[1]
      resSub = exprSelec[0] - exprSelec[1]
      resMult = exprSelec[0] * exprSelec[1]
      if resSoma == exprSelec[2] or resSub == exprSelec[2] or resMult == exprSelec[2]:
        perdeu.append(jogador)
    else:
      if op == "+":
        res = exprSelec[0] + exprSelec[1]
      elif op == "-":
        res = exprSelec[0] - exprSelec[1]
      elif op == "*":
        res = exprSelec[0] * exprSelec[1]
      
      if res != exprSelec[2]:
        perdeu.append(jogador)
  
  if len(perdeu) == n:
    print("None Shall Pass!")
  elif len(perdeu) == 0:
    print("You Shall All Pass!")
  else:
    perdeu.sort()
    saida = " ".join(perdeu)
    print(saida)
