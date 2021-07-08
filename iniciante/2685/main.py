while True:
  try:
    g = int(input())
  except EOFError:
    break

  if 0 <= g < 90 or g == 360:
    print("Bom Dia!!")
  elif 90 <= g < 180:
    print("Boa Tarde!!")
  elif 180 <= g < 270:
    print("Boa Noite!!")
  elif 270 <= g < 360:
    print("De Madrugada!!")