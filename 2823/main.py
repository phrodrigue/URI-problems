n = int(input())

cnt = 0

for _ in range(n):
  c, p = [float(x) for x in input().split()]
  cnt += c/p

if cnt > 1:
  print("FAIL")
else:
  print("OK")