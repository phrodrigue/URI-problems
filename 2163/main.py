N, M = [int(x) for x in input().split()]
MATRIZ = []
for _ in range(N):
  MATRIZ.append([int(x) for x in input().split()])

achou = False
coord = [0, 0]
for l in range(1, N - 1):
  for c in range(1, M - 1):
    if MATRIZ[l][c] == 42:
      if MATRIZ[l - 1][c - 1] == \
          MATRIZ[l - 1][c] == \
          MATRIZ[l - 1][c + 1] == \
          MATRIZ[l][c - 1] == \
          MATRIZ[l][c + 1] == \
          MATRIZ[l + 1][c - 1] == \
          MATRIZ[l + 1][c] == \
          MATRIZ[l + 1][c + 1] == 7:
        achou = True
        coord = [l + 1, c + 1]
        break
  if achou:
    break

print(coord[0], coord[1])