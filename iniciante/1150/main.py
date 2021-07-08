x = int(input())
z = 0

while z <= x:
    z = int(input())

soma = 0
c = 0
while soma <= z:
    soma += x
    x += 1
    c += 1

print(c)
