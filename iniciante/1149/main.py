lista = [int(x) for x in input().split()]
A = lista[0]
N = lista[-1]
soma = 0
for i in range(N):
    soma += A + i

print(soma)
