c = 1
saida = ""
while True:
  n = int(input())
  
  if not n:
    break

  linha = input()
  saida += f"Teste {c}:\n"
  res = 0
  
  num = "+"
  for x in linha:
    if x in '+-':
      res += int(num)
      num = x
    else:
      num += x
    
  res += int(num)
  saida += f"{res}\n\n"
  
  c += 1

print(saida[:-2])