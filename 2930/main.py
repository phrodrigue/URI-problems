e, d = [int(x) for x in input().split()]

if e > d or e >= 24:
  saida = "Eu odeio a professora!"
elif e + 2 < d:
  saida = "Muito bem! Apresenta antes do Natal!"
else:
  saida =  "Parece o trabalho do meu filho!"
  if e + 2 < 24:
    saida += "\nTCC Apresentado!"
  else:
    saida += "\nFail! Entao eh nataaaaal!"

print(saida)