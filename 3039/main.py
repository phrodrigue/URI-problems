n = int(input())
carrinho = boneca = 0

for _ in range(n):
  c = input().split()
  if c[1] == "M":
    carrinho += 1
  else:
    boneca += 1

print(f"{carrinho} carrinhos\n{boneca} bonecas")
