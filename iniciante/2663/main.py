n = int(input())
max = int(input())

competidores = []
for _ in range(n):
  competidores.append(int(input()))

competidores.sort(reverse=True)
saida = competidores[:max]

for c in range(max, n):
  if competidores[c] == saida[-1]:
    saida.append(competidores[c])
  else:
    break

print(len(saida))