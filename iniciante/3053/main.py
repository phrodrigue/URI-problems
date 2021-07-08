posicoes = {
  "A": False,
  "B": False,
  "C": False,
}

n = int(input())
ini = input()
posicoes[ini] = True

for _ in range(n):
  tipo = input()
  if tipo == "1":
    i = "A"
    f = "B"
  elif tipo == "2":
    i = "C"
    f = "B"
  else:
    i = "A"
    f = "C"
  
  x = posicoes[i]
  posicoes[i] = posicoes[f]
  posicoes[f] = x

for p in posicoes:
  if posicoes[p]:
    print(p)
    break