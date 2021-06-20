import re

n = int(input())

for _ in range(n):
  v = int(input())
  
  if v != 0:
    b = f"{v:050b}"
    
    res = re.findall(r"1{1,}", b)
    saida = list(map(len, res))
    print(max(saida))
  else:
    print(0)