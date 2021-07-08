saida = ""
while True:
  n = int(input())
  if n == 0:
    break
  
  M = []
  l = 1
  maior = 1

  for L in range(n):
    linha = []
    c = 1
    for C in range(0, n):
      valor = l * c
      linha.append(valor)
      maior = len(str(valor)) if len(str(valor)) >= maior else maior
      c *= 2

    M.append(linha)
    l *= 2
  
  for l in M:
    li = ""
    for item in l:
      li += f"{item:{maior}} "

    saida += li[:-1] + "\n"
  
  saida += "\n"
print(saida[:-1])
