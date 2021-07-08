while True:
  try:
    n = int(input())
    palavras = []
    for _ in range(n):
      palavras.append(input())

    e = int(input())
    for _ in range(e):
      tot = maior = 0
      pesquisa = input()
      for p in palavras:
        if pesquisa == p[:len(pesquisa)]:
          t = len(p)
          maior = t if t > maior else maior
          tot += 1
      
      if tot:
        saida = f"{tot} {maior}"
      else:
        saida = -1
        
      print(saida)
  except EOFError:
    break
