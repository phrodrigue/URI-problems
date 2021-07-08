n = int(input())
lista = list(map(lambda x: int(x), input().split()))
pico = 0
igual = True
for i in range(1, n):
  p = 2 if lista[i] > lista[i - 1] else 1 if lista[i] < lista[i - 1] else 0
  
  if not p or p == pico:
    igual = False
    break
  else:
    pico = p

print(1 if igual else 0)