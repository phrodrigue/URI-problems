n = int(input())
r = list(map(int, input().split()))
saida = 0
for i in range(1, n):
  if r[i] < r[i - 1]:
    saida = i + 1
    break
  
print(saida)