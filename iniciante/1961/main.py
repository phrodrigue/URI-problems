P, N = [int(x) for x in input().split()]
alturas = [int(x) for x in input().split()]
res = "YOU WIN"
for a in range(N - 1):
  if abs(alturas[a] - alturas[a + 1]) > P:
    res = "GAME OVER"
    break

print(res)