n = int(input())

for _ in range(n):
  x = int(input())
  primo = True

  for i in range(2, x):
    if x % i == 0:
      primo = False
  
  if primo:
    print(x, "eh primo")
  else:
    print(x, "nao eh primo")
