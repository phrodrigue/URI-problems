maior = indice = 0

for i in range(1, 101):
  n = int(input())
  if n > maior:
    maior = n
    indice = i

print(maior)
print(indice)