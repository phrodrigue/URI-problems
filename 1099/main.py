n = int(input())

for _ in range(n):
  X, Y = [int(x) for x in input().split()]
  menor = X if X < Y else Y
  maior = X if X > Y else Y
  soma = 0
  for num in range(menor + 1, maior):
    if num % 2 != 0:
      soma += num
  print(soma)