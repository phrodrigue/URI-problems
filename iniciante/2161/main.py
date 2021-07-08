n = int(input())

def calc(n):
  if n == 0:
    return 0
  r = calc(n - 1)
  x = 1 / r if r != 0 else 0
  return 6 + x

r = calc(n)
x = 1 / r if r != 0 else 0
saida = 3 + x
print(f"{saida:0.10f}")