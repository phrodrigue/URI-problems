n = int(input())

for _ in range(n):
  e = list(map(int, input().split()))
  s = sum(e[1:])
  print(s - (e[0] - 1))