e, f, c = list(map(int, input().split()))

totGarrafas = e + f
totBebidas = 0

while totGarrafas >= c:
  compra = totGarrafas // c
  totBebidas += compra
  totGarrafas = compra + (totGarrafas % c)

print(totBebidas)