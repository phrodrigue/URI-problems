while True:
  X, Y = [int(x) for x in input().split()]

  if X == 0 or Y == 0:
    break

  if X > 0 and Y > 0:
    print("primeiro")
  elif X > 0 and Y < 0:
    print("quarto")
  elif X < 0 and Y < 0:
    print("terceiro")
  else:
    print("segundo")
