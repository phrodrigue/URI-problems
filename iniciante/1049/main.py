carac1 = input()
carac2 = input()
carac3 = input()

if carac1 == "vertebrado":
  if carac2 == "ave":
    if carac3 == "carnivoro":
      print("aguia")
    else:
      print("pomba")
  else:
    if carac3 == "onivoro":
      print("homem")
    else:
      print("vaca")

else:
  if carac2 == "inseto":
    if carac3 == "hematofago":
      print("pulga")
    else:
      print("lagarta")
  else:
    if carac3 == "hematofago":
      print("sanguessuga")
    else:
      print("minhoca")