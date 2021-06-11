n = int(input())

for _ in range(n):
  jog1, eJog1, jog2, eJog2 = input().split()
  n1, n2 = list(map(lambda x: int(x), input().split()))
  res = n1 + n2
  vencedor = jog1 if eJog1 == "PAR" and res % 2 == 0 or eJog1 == "IMPAR" and res % 2 != 0 else jog2

  print(vencedor)