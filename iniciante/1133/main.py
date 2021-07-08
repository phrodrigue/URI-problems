x = int(input())
y = int(input())
maior = x if x > y else y
menor = x if x < y else y

for n in range(menor + 1, maior):
  if n % 5 == 2 or n % 5 == 3:
    print(n)