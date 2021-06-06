n = int(input())

for _ in range(n):
  a, b, c = [float(x) for x in input().split()]
  media = (a * 2 + b * 3 + c * 5) / 10
  print(round(media, 1))