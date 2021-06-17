vence = {
  "pedra": "tesoura",
  "papel": "pedra",
  "tesoura": "papel"
}

saidas = [
  "Os atributos dos monstros vao ser inteligencia, sabedoria...",
  "Iron Maiden's gonna get you, no matter how far!",
  "Urano perdeu algo muito precioso...",
  "Putz vei, o Leo ta demorando muito pra jogar..."
]

while True:
  try:
    jogadas = input().split()
  except EOFError:
    break

  vencedores = []

  for um in range(3):
    for dois in range(3):
      if vence[jogadas[um]] == jogadas[dois] and um not in vencedores:
          vencedores.append(um)
          
  saida = saidas[vencedores[0]] if len(vencedores) == 1 else saidas[3]
  print(saida)