while True:
  try:
    n, id = [int(x) for x in input().split()]
  except EOFError:
    break
  
  tot = 0
  for _ in range(n):
    idJ, jogo = [int(x) for x in input().split()]
    if idJ == id and jogo == 0:
      tot += 1
  
  print(tot)
