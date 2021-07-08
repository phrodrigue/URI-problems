x, y = [int(w) for w in input().split()]
res = ''

for n in range(1, y + 1):
  res += str(n)
  if n % x == 0 and n != y:
    res += "\n"
  elif n != y:
    res += " "

print(res)