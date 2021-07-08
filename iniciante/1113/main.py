while True:
  X, Y = [int(x) for x in input().split()]

  if X == Y:
    break

  if X > Y:
    print("Decrescente")
  else:
    print("Crescente")
