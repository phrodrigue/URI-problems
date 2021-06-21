a = "abcdefghijklmnopqrstuvwxyz"
while True:
  try:
    n = int(input())
  except EOFError:
    break

  for _ in range(n):
    linha = input().split()
    c = (len(linha) - 1) * 3
    letra = a[c + len(linha[0]) - 1]
    print(letra)