n, m = [int(x) for x in input().split()]

frutas = {}

for _ in range(n):
  frutas[input().lower()] = False

for _ in range(m):
  linha = input().lower()

  for fruta in frutas:
    if not frutas[fruta]:
      if fruta in linha or fruta[::-1] in linha:
        frutas[fruta] = True

for fruta in frutas:
  s = "Sheldon come a fruta" if frutas[fruta] else "Sheldon detesta a fruta"
  print(s, fruta)