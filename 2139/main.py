meses = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 25]
while True:
  try:
    m, d = [int(x) for x in input().split()]
    m -= 1
  except EOFError:
    break

  dias = (meses[m] - d) + sum(meses[m + 1:])
  
  if dias < 0:
    print("Ja passou!")
  elif dias == 0:
    print("E natal!")
  elif dias ==1:
    print("E vespera de natal!")
  else:
    print(f"Faltam {dias} dias para o natal!")
