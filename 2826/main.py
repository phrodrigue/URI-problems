alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

a = input()
b = input()
ta = len(a)
tb = len(b)
menor = ta
res = a + "\n" + b

if ta > tb:
    res = b + "\n" + a
    menor = tb

for i in range(menor):
  pa = alfabeto.index(a[i])
  pb = alfabeto.index(b[i])

  if pa != pb:
    if pa < pb:
      res = a + "\n" + b
    elif pa > pb:
      res = b + "\n" + a

    break

print(res)