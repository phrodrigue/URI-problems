c = 1
saida = ""

while True:
  x1, y1, x2, y2 = [int(x) for x in input().split()]
  
  if x1 == y1 == x2 == y2 == 0 :
    break

  n = int(input())
  tot = 0
  
  for _ in range(n):
    x, y = [int(x) for x in input().split()]
    if x1 <= x <= x2 and y2 <= y <= y1:
      tot += 1
  
  saida += f"Teste {c}\n{tot}\n"
  c += 1

print(saida[:-1])