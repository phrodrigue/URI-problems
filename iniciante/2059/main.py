p, j1, j2, r, a = [int(x) for x in input().split()]
par = 1 if (j1 + j2) % 2 == 0 else 0

if r and a:
  print("Jogador 2 ganha!")
elif (r and not a) or (not r and a) or (p and par) or (not p and not par):
  print("Jogador 1 ganha!")
else:
  print("Jogador 2 ganha!")
