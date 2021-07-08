while True:
  try:
    n = int(input())
    M, L = [int(x) for x in input().split()]
    dM = []
    dL = []
    for _ in range(M):
      dM.append([int(x) for x in input().split()])
    for _ in range(L):
      dL.append([int(x) for x in input().split()])
    cM, cL = [int(x) - 1 for x in input().split()]
    a = int(input()) - 1

  except EOFError:
    break

  aM = dM[cM][a]
  aL = dL[cL][a]
  print("Marcos" if aM > aL else "Leonardo" if aL > aM else "Empate")