while True:
  try:
    n,m = [int(x) for x in input().split()]
  except EOFError:
    break

  city = []
  for i in range(n):
    l = [int(x) for x in input().split()]
    for j in range(m):
      if l[j] == 1:
        jog = (i, j)
      elif l[j] == 2:
        anal = (i, j)

  dist = abs(jog[0] - anal[0]) + abs(jog[1] - anal[1])
  print(dist)
