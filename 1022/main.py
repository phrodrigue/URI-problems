def simplifica(C, N, D):
  menor = N if N < D else D
  if not C or N == 0 or D == 0:
    return [C, N, D]
  cont = False
  for n in range(2, abs(menor) + 1):
    if N % n == 0 and D % n == 0:
      nf = int(N / n)
      df = int(D / n)
      cont, N, D = simplifica(True, nf, df)
      break

  return [cont, N, D]

n = int(input())
for _ in range(n):
  N1, z, D1, oper, N2, y, D2 = input().split()
  N1, D1, N2, D2 = [int(x) for x in [N1, D1, N2, D2]]
 
  if oper == "+":
    Nf = N1*D2 + N2*D1
    Df = D1*D2    
  elif oper == "-":
    Nf = N1*D2 - N2*D1
    Df = D1*D2    
  elif oper == "*":
    Nf = N1*N2
    Df = D1*D2    
  else:
    Nf = N1*D2
    Df = N2*D1    
  
  c, np, dp = simplifica(True, Nf, Df)
  res = f"{Nf}/{Df} = {np}/{dp}"
  
  print(res)
