n = int(input())
estrelas = list(map(lambda x: int(x), input().split()))
orig = estrelas[:]
i = 0

while True:
  try:
    qtd = estrelas[i]
  except IndexError:
    break

  if i < 0 or qtd == 0:
    break

  estrelas[i] -= 1
  if qtd % 2 != 0:
    i += 1
  else:
    i -= 1

dif = 0
for c, i in enumerate(orig):
  if i != estrelas[c]:
    dif += 1

print(dif, sum(estrelas))
