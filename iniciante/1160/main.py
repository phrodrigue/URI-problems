T = int(input())

for _ in range(T):
  entrada = input().split()
  PA = int(entrada[0])
  PB = int(entrada[1])
  G1 = 1 + (float(entrada[2]) / 100)
  G2 = 1 + (float(entrada[3]) / 100)
  anos = 0

  while PA <= PB:
    PA = int(PA * G1)
    PB = int(PB * G2)
    anos += 1

    if anos == 101:
      break
  
  saida = f"{anos} anos." if anos <= 100 else "Mais de 1 seculo."
  print(saida)