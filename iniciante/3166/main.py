def verificaDiagonal(diagonal, tipo):
  for palavra in palavras:
    if not palavras[palavra]["achou"] and palavra in diagonal or palavra[::-1] in diagonal:
      palavras[palavra]["achou"] = True
      palavras[palavra]["txt"] = saidas[tipo].format(palavra)
      

saidas = [
  '1 Palavra "{}" na diagonal principal',
  '2 Palavra "{}" acima da diagonal principal',
  '3 Palavra "{}" abaixo da diagonal principal',
  '4 Palavra "{}" inexistente',
]

n, l, c = [int(x) for x in input().split()]

palavras = {}
for _ in range(n):
  entrada = input().lower()
  palavras[entrada] = {"achou": False, "txt": saidas[3].format(entrada)}

matriz = []
for _ in range(l):
  matriz.append(input().lower())

p = ""
## DIAGONAL PRINCIAPL
for i in range(l):
  p += matriz[i][i]
verificaDiagonal(p, 0)

##  ACIMA DA DIAGONAL PRINCIPAL
lc = 0
for cc in range(1, c): #inicia uma diagonal
  pal = ""
  li = lc
  ci = cc
  while True: # pega todos caracteres da diagonal
    try:
      pal += matriz[li][ci]
    except IndexError:
      break
    ci += 1
    li += 1
  verificaDiagonal(pal, 1)

##  ABAIXO DA DIAGONAL PRINCIPAL
cc = 0
for lc in range(1, l): #inicia uma diagonal
  pal = ""
  li = lc
  ci = cc
  while True: # pega todos caracteres da diagonal
    try:
      pal += matriz[li][ci]
    except IndexError:
      break
    ci += 1
    li += 1
  verificaDiagonal(pal, 2)


saida = ""
for pa in palavras:
  saida += palavras[pa]["txt"] + "\n"
print(saida[:-1])