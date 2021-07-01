n = int(input())

for _ in range(n):
  t, k = [int(x) for x in input().split()]
  print((t % k) + (t // k))