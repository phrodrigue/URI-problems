n = int(input())

for _ in range(n):
  ano = int(input())
  anoB = 2015 - ano
  p = "D.C."
  if anoB <= 0:
    anoB = abs(anoB) + 1
    p = "A.C."
  
  resp = f"{anoB} {p}"
  print(resp)