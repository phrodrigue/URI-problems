def verifica(u, comp):
  al = "abcdefghjklmnopqrstuvwxyz".upper()
  if comp in u:
    try:
      if u[u.index(comp) + len(comp)] in al:
        return True
      else:
        return False
    except:
      return True
      
  else:
    return False

n = int(input())
saida = ""

for _ in range(n):
  p = int(input())
  compostos = []
  for i in range(p):
    e = input()
    compostos.append(e)
    
  t = int(input())
  temp = ""
  for i in range(t):
    u = input()
    for comp in compostos:
      res = verifica(u, comp)
      if res:
        break
    
    if res:
      temp += f"Abortar\n"
    else:
      temp += f"Prossiga\n"

  saida += f"{temp}\n"

print(saida[:-1])