runas = {}
n, g = [int(x) for x in input().split()]

for _ in range(n):
  runa, v = input().split()
  runas[runa] = int(v)

x = int(input())

r = input().split()

tot = 0
for runa in r:
  tot += runas[runa]

saida = f"{tot}\n"
saida += "My precioooous" if tot < g else "You shall pass!"
print(saida)
