def criaMeio(txt):
  t = "|" + " " * 8 + f"{txt:<29}|"
  return t

t = 39

linha = "-" * t

print(linha)
print(criaMeio("Roberto"))
print(criaMeio(" "))
print(criaMeio("5786"))
print(criaMeio(" "))
print(criaMeio("UNIFEI"))
print(linha)