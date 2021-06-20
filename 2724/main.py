import re

def verifica(u, comp):
  padrao = comp + r"([A-Z]|$)"
  r = re.match(padrao, u)
  #print(repr(padrao))
  return r

n = int(input())

for _ in range(n):
  p = int(input())
  compostos = []
  for i in range(p):
    e = input()
    compostos.append(e)
    
  t = int(input())
  
  for i in range(t):
    u = input()
    #print(repr(u))
    perigoso = False
    for comp in compostos:
      res = verifica(u, comp)
      if res:
        perigoso = True
        break
    print(perigoso)
  print()