linguas = {
  "esquerda": "ingles",
  "direita": "frances",
  "nenhuma": "portugues",
  "as duas": "caiu",
}

while True:
  try:
    print(linguas[input()])
  except EOFError:
    break