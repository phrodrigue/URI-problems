while True:
  try:
    n = int(input())
  except EOFError:
    break

  MATRIZ = ""

  for L in range(n):
    linha = ""
    for C in range(n):
      valor = "2" if L + C == n - 1 else "1" if L == C else "3"
      linha += valor
    MATRIZ += linha + "\n"
  
  print(MATRIZ[:-1])
