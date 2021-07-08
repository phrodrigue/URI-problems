n = int(input())
pontoFraco = {
  "ataque": [],
  "pedra": ["ataque"],
  "papel": ["pedra", "ataque"],
}

for _ in range(n):
  jog1 = input()
  jog2 = input()

  if jog1 == jog2:
    if jog1 == "ataque":
      saida = "Aniquilacao mutua"
    elif jog1 == "pedra":
      saida = "Sem ganhador"
    else:
      saida = "Ambos venceram"
  else:
    if jog1 in pontoFraco[jog2]:
      saida = "Jogador 1 venceu"
    else:
      saida = "Jogador 2 venceu"
  
  print(saida)