abas, acoes = [int(x) for x in input().split()]

for _ in range(acoes):
  acao = input()
  if acao == "fechou":
    abas += 1
  else:
    abas -= 1

print(abas)