def descriptografa(palavraOrig, palavraChave):
  final = ""

  for i in range(len(palavraOrig)):
    final += allFabeto[palavraChave[i]][alfabeto.index(palavraOrig[i])]
  
  return final

alfabeto = "abcdefghijklmnopqrstuvwxyz"

allFabeto = {"a": alfabeto[:]}
for i in range(1, len(alfabeto)):
  allFabeto[alfabeto[i]] = alfabeto[i:] + alfabeto[:i]
  

k = input()
n = int(input())
t = len(k)
for _ in range(n):
  frase = input().split()
  novaFrase = ""
  c = 0

  for palavra in frase:
    if palavra[0] not in "aeiou":
      crip = ""
      for letra in palavra:
        crip += k[c]
        c = c + 1 if c + 1 < t else 0
      novaFrase += descriptografa(palavra, crip) + " "
    else:
      novaFrase += palavra + " "

  print(novaFrase[:-1])