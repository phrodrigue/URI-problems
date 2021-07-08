notas = [100, 50, 20, 10, 5, 2]

while True:
  N, M = [int(x) for x in input().split()]
  troco = M - N

  if N == M == 0:
    break
  
  possivel = False
  for nota in notas:
    t = troco
    if t - nota > 0:
      t -= nota
      for n in notas:
        if t - n == 0:
          possivel = True
          break
    if possivel:
      break
  
  saida = "possible" if possivel else "impossible"
  print(saida)
