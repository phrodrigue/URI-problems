c = 1
while True:
  try:
    n1 = input()
    n2 = input()
  except EOFError:
    break

  tot = 0
  pos = 0
  ln1 = len(n1)
  for l in range(len(n2)):
    if n2[l:l+ln1] == n1:
      tot += 1
      pos = l + 1
  
  print(f"Caso #{c}:")
  if tot:
    print(f"Qtd.Subsequencias: {tot}")
    print("Pos:", pos)
  else:
    print("Nao existe subsequencia")
  print()
  c+= 1