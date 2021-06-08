def imprimeLista(txt, lista):
  for n, i in enumerate(lista):
    print(f"{txt}[{n}] = {i}")
  return []

par = []
impar = []

for i in range(15):
  x = int(input())

  if x % 2 == 0:
    par.append(x)
    if len(par) == 5:
      par = imprimeLista("par", par)
  else:
    impar.append(x)
    if len(impar) == 5:
      impar = imprimeLista("impar", impar)
  
imprimeLista("impar", impar)
imprimeLista("par", par)