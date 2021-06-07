while True:
  notas = []

  while len(notas) < 2:
    nota = float(input())

    if 0 <= nota <= 10:
      notas.append(nota)
    else:
      print("nota invalida")

  print(f"media = {sum(notas) / len(notas):0.2f}")

  while True:
    print("novo calculo (1-sim 2-nao)")
    o = input()
    if o == "1":
      outra = True
      break
    elif o == "2":
      outra = False
      break
  
  if not outra:
    break
