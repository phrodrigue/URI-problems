lista = list(map(int, input().split()));
a = False
for i in range(3):
  item = lista[i]
  for c in range(3):
    if i != c and item - lista[c] == 0:
      a = True
      break
    
  if item - (sum(lista) - item) == 0:
    a = True

  if a:
    break

print("S" if a else "N")