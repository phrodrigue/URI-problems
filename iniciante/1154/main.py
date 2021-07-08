idades = []
while True:
  i = int(input())
  if i < 0:
    break
  idades.append(i)

print(f"{sum(idades) / len(idades):0.2f}")