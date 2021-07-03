muda = [
  {1: 1, 2: 2},
  {0: 1, 2: 1},
  {0: 2, 1: 1}
]

while True:
  n = int(input())

  if not n:
    break

  toques = 0
  atual = 1
  for _ in range(n):
    linha = list(map(int, input().split()))

    if 1 in linha:
      vazia = linha.index(0)
      if vazia != atual:
        toques += muda[atual][vazia]
        atual = vazia
  
  print(toques)