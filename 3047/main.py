m = int(input())
a = int(input())
b = int(input())
c = m - (a + b)
maior = a if a > b else b
maior = maior if maior > c else c

print(maior)