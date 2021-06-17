while True:
  try:
    n = int(input())
  except EOFError:
    break

  vm = 0
  for i in range(n):
    t, s = [int(x) for x in input().split()]
    if s / t > vm:
      vm = s/t
      print(1 + i)