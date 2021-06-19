andares = []
for _ in range(3):
  andares.append(int(input()))

minutos = [
  andares[1] * 2 + andares[2] * 4,
  andares[0] * 2 + andares[2] * 2,
  andares[0] * 4 + andares[1] * 2,
]
print(min(minutos))