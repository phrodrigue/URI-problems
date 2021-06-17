while True:
  try:
    n, aMin, aMax = [int(x) for x in input().split()]
  except EOFError:
    break

  tot = 0
  for _ in range(n):
    a = int(input())
    if aMin <= a <= aMax:
      tot += 1

  print(tot)