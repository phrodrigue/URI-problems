jipes = turistas = 0

while True:
  entrada = input()
  if entrada == "ABEND":
    break

  tipo, t = entrada.split()

  if tipo == "SALIDA":
    jipes += 1
    turistas += int(t)
  else:
    jipes -= 1
    turistas -= int(t)

print(turistas)
print(jipes)