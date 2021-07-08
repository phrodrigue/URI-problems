while True:
  try:
    n = int(input())
  except EOFError:
    break

  saida = 11
  for _ in range(n):
    t = float(input())
    if t < saida:
      saida = t
  
  print(f"{saida:0.2f}")