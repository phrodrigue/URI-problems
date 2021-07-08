from math import pow

l = [int(x) for x in input().split()]
l.sort()

if l[0] + l[1] > l[2]:
  r = "Valido-"
  if l[0] == l[1] == l[2]:
    r += "Equilatero"
  elif l[0] != l[1] != l[2]:
    r += "Escaleno"
  elif l[0] == l[1] or l[1] == l[2]:
    r += "Isoceles"
  
  r += "\nRetangulo: "
  if pow(l[2], 2) == pow(l[1], 2) + pow(l[0], 2):
    r += "S"
  else:
    r += "N"
  
  print(r)
else:
  print("Invalido")