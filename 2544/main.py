while True:
  try:
    n = int(input())
  except EOFError:
    break
  
  saida = 0
  while n >= 2:
    n /= 2
    saida += 1

  print(saida)