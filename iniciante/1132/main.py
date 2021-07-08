x = int(input())
y = int(input())

maior = x if x > y else y
menor = x if x < y else y
soma = 0

for n in range(menor, maior + 1):
  if n % 13 != 0:
    soma += n

print(soma)
