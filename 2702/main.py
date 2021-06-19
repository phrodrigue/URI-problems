o = list(map(int, input().split()))
u = list(map(int, input().split()))
tot = 0
for i in range(3):
  if u[i] > o[i]:
    tot += u[i] - o[i]

print(tot)