while True:
  try:
    graus = float(input())
  except EOFError:
    break

  if 0 <= graus < 90 or graus == 360:
    print("Bom Dia!!")
  elif 90 <= graus < 180:
    print("Boa Tarde!!")
  elif 180 <= graus < 270:
    print("Boa Noite!!")
  elif 270 <= graus < 360:
    print("De Madrugada!!")

  segPorGrau = 240
  totSegundos = int(segPorGrau * graus)

  h = 0
  while totSegundos >= 3600:
    h += 1
    totSegundos -= 3600
  
  h = h + 6 if h < 18 else h - 18
  
  m = 0
  while totSegundos >= 60:
    m += 1
    totSegundos -= 60

  print(f"{h:0>2}:{m:0>2}:{totSegundos:0>2}")