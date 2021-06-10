while True:
  try:
    n = int(input())
  except EOFError:
    break

  MATRIZ = ""

  for L in range(n):
    linha = ""
    for C in range(n):
      lim = int(n / 3)
      if L + C == n - 1 and L == C:
        valor = "4"
      elif L >= lim and C >= lim and L < n - lim and C < n - lim:
        valor = "1"
      elif L + C == n - 1:
        valor = "3"
      elif L == C:
        valor = "2"
      else:
        valor = "0"
        
      linha += valor
    MATRIZ += linha + "\n"
  
  print(MATRIZ[:-1])
  print()
