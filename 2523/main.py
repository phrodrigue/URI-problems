while True:
  try:
    alf = input()
    n = input()
    letras = input().split()
  except EOFError:
    break

  frase = list(map(lambda x: alf[int(x) - 1], letras))
  print("".join(frase))