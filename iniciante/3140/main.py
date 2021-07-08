imprime = False
while True:
  linha = input()
  
  if "</body>" in linha:
    break

  if imprime:
    print(linha)

  if "<body>" in linha:
    imprime = True
