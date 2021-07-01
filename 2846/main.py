n = int(input())

fib = [0, 1]
fibnot = []
i = 1

while len(fibnot) < n:
  soma = fib[-2] + fib[-1]

  if i == soma:
    fib.append(i)
  else:
    fibnot.append(i)

  i += 1
  
print(fibnot[-1])
