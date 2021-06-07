combustiveis = {
  "1": {"nome": "Alcool", "qtd": 0},
  "2": {"nome": "Gasolina", "qtd": 0},
  "3": {"nome": "Diesel", "qtd": 0},
}

while True:
  tipo = input()
  if tipo == "4":
    break

  try:
    combustiveis[tipo]["qtd"] += 1
  except KeyError:
    pass

print("MUITO OBRIGADO")
for tipo in combustiveis:
  print(f"{combustiveis[tipo]['nome']}: {combustiveis[tipo]['qtd']}")
