def converte(num, c):
  l = {
    1: {1: 'I', 5: 'V', 10: 'X'},
    10: {1: 'X', 5: 'L', 10: 'C'},
    100: {1: 'C', 5: 'D', 10: 'M'},
  }
  ls = l[c]
  
  unid = ls[1]
  base = "" if num <= 5 else ls[5]
  teto = ls[5] if num <= 5 else ls[10]
  num = num if num <= 5 else num - 5
  
  if num == 1:
    res = base + unid
  elif num == 2:
    res = base + unid * 2
  elif num == 3:
    res = base + unid * 3
  elif num == 4:
    res = unid + teto
  else:
    res = teto
    
  return res
  
  
entrada = int(input())
saida = ""
c = 100
while True:
  valor = int(entrada // c)
  entrada -= valor * c

  if valor > 0:
    saida += converte(valor, c)
  
  c = int(c / 10)
  if entrada < 1:
    break

print(saida)