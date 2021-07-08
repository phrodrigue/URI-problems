n = int(input())

for _ in range(n):
  hdg = list(map(int, input().split()))

  if 200 <= hdg[0] <= 300 and hdg[1] >= 50 and hdg[2] >= 150:
    print("Sim")
  else:
    print("Nao")