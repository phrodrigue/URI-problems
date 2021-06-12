cardapio = {
  1001: 1.50,
  1002: 2.50,
  1003: 3.50,
  1004: 4.50,
  1005: 5.50,
}

n = int(input())
tot = 0
for _ in range(n):
  prod, qtd = list(map(lambda x: int(x), input().split()))
  tot += cardapio[prod] * qtd

print(f"{tot:0.2f}")