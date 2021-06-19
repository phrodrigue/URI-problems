import re
n = int(input())
padrao = r"^[A-Z]{3}-\d{4}$"
dias = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

for _ in range(n):
  placa = input()

  if bool(re.match(padrao, placa)):
    if placa[-1] == "0":
      dia = dias[4]
    else:
      d = int((int(placa[-1]) + 1) / 2) - 1
      dia = dias[d]

    print(dia)
  else:
    print("FAILURE")
