while True:
  try:
    a, b, perc = [int(x) for x in input().split()]
  except:
    break
  
  perc /= 100
  area = a * b
  lado = (area / perc) ** (1/2)

  print(int(lado))