n = int(input())

for _ in range(n):
  t = int(input())
  lista = input().split()
  impares = []
  
  for i in lista:
    num = int(i)
    if num % 2 == 1:
      impares.append(num)
      
  impares.sort()
  saida = ""
  
  t = len(impares)
  
  while t > 0:
    saida += str(impares.pop()) + " "
    if t > 1:
      saida += str(impares.pop(0)) + " "
    t -= 2
    
  print(saida[:-1])