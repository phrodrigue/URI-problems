def calc(n):
  if n == 0:
    return 0
  c = calc(n - 1)
  x = 1 / c if c else 0
  return 2 + x

n = int(input())
c = calc(n)
x = 1 / c if c else 0
saida = 1 + x
print(f"{saida:0.10f}")