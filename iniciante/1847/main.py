p, s, t = [int(x) for x in input().split()]
diffPS = s - p
diffST = t - s

if diffPS < 0:
  if diffST >= 0 or diffST > diffPS:
    print(":)")
  else:
    print(":(")
elif diffPS > 0:
  if diffST <= 0 or diffST < diffPS:
    print(":(")
  else:
    print(":)")
else:
  if diffST > 0:
    print(":)")
  else:
    print(":(")
