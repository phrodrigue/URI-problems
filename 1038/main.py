precos = [4, 4.5, 5, 2, 1.5]

cod, qtd = [int(x) for x in input().split()]

preco = precos[cod - 1] * qtd

print(f"Total: R$ {preco:0.2f}")
