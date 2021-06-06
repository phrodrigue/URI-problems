faixas = [
    {"intervalo": 1000, "perc": 0.08},
    {"intervalo": 1500, "perc": 0.18},
    {"intervalo": 0, "perc": 0.28},
]

salario = float(input())
s = salario
impostoAPagar = 0

if salario <= 2000:
    print("Isento")
else:
  salario -= 2000
  for faixa in faixas:
    if salario > faixa["intervalo"]:
      base = faixa["intervalo"]
      salario -= faixa["intervalo"]
      parar = False
    else:
      base = salario
      parar = True

    impostoAPagar += base * faixa["perc"]

    if parar:
      break

  print(f"R$ {impostoAPagar:0.2f}")
