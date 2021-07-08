n = int(input())

for _ in range(n):
  n, m = [int(x) for x in input().split()]
  res = n ** m
  print(len(str(res)))