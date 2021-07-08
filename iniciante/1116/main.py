n = int(input())

for _ in range(n):
  X, Y = [int(x) for x in input().split()]

  try:
    print(round(X / Y, 1))
  except:
    print("divisao impossivel")