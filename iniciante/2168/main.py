n = int(input())
M = []
for _ in range(n + 1):
  M.append([int(x) for x in input().split()])

for l in range(1, n+1):
  L = ""
  for c in range(1, n+1):
    cam = [
      M[l - 1][c - 1],
      M[l - 1][c],
      M[l][c - 1],
      M[l][c],
    ]
    L += "S" if sum(cam) >= 2 else "U"
  print(L)
