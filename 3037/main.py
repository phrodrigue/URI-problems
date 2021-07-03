n = int(input())

for _ in range(n):
  ptsJoao = ptsMaria = 0

  for i in range(3):
    xd = input().split()
    ptsJoao += int(xd[0]) * int(xd[1])
  
  for i in range(3):
    xd = input().split()
    ptsMaria += int(xd[0]) * int(xd[1])

  print("JOAO" if ptsJoao > ptsMaria else "MARIA")