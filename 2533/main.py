while True:
  try:
    n = int(input())
  except EOFError:
    break
  
  den = div = 0
  for _ in range(n):
    n, c = [int(x) for x in input().split()]
    den += n * c
    div += c
  
  saida = den / (div * 100)
  print(f"{saida:0.4f}")