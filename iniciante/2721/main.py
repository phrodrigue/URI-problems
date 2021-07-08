renas = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]

bolas = [int(x) for x in input().split()]
t = sum(bolas) % 9
r = renas[t - 1]
print(r)