n = int(input())

a = 0
b = 1
saida = f"{a} {b} "
for i in range(n - 2):
  x = a + b
  a = b
  b = x

  saida += f"{x} "
  
print(saida[:-1])