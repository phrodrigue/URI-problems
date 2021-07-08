joias = []

while True:
  try:
    j = input()
  except EOFError:
    break

  if j not in joias:
    joias.append(j)

print(len(joias))