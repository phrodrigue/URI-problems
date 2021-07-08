n = int(input())
l = list(map(lambda x: int(x), input().split()))

multiplos = {2: 0, 3: 0, 4: 0, 5: 0}

for i in l:
  for num in multiplos:
    if i % num == 0:
      multiplos[num] += 1

for num in multiplos:
  print(f"{multiplos[num]} Multiplo(s) de {num}")