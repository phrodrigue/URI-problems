while True:
  try:
    n = int(input())
    trab = [int(x) for x in input().split()]
  except EOFError:
    break

  p = sum(trab[:1])
  s = sum(trab[1:])
  menor = abs(s - p)
  for c in range(1, len(trab)):
    item = trab[c]
    p += item
    s -= item
    
    diff = abs(s - p)
    
    if diff < menor:
      menor = diff
    if p > s:
      break

  print(menor)
