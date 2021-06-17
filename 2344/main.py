n = int(input())
conceitos = {0: "E", 35: "D", 60: "C", 85: "B", 100: "A"}
for c in conceitos:
  if n <= c:
    print(conceitos[c])
    break