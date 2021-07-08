n, c, m = [int(x) for x in input().split()]
carimbadas = [int(x) for x in input().split()]
compradas = [int(x) for x in input().split()]

tot = 0

for i in carimbadas:
  if i in compradas:
    tot += 1

print(c - tot)
