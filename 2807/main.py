n = int(input())

fib = [0, 1]
for i in range(2, n + 1):
  x = fib[i - 2] + fib[i - 1]
  fib.append(x)

f = fib[1:]
print(' '.join([str(x) for x in f[::-1]]))