while True:
  try:
    r = int(input())
  except EOFError:
    break

  if r == 0:
    print("vai ter copa!")
  else:
    print("vai ter duas!")
