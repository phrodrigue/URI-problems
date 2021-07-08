n = int(input())
m = int(input())
fig = []

for _ in range(m):
  x = int(input())
  if x not in fig:
    fig.append(x)

print(n - len(fig))