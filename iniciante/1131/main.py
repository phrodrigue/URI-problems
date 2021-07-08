cont = "1"

vi = 0
vg = 0
empates = 0
tot = 0

while cont == "1":
  i, g = [int(x) for x in input().split()]
  tot += 1
  if i > g:
    vi += 1
  elif i < g:
    vg += 1
  else:
    empates += 1

  print("Novo grenal (1-sim 2-nao)")
  cont = input()

print(tot, "grenais")
print(f"Inter:{vi}")
print(f"Gremio:{vg}")
print(f"Empates:{empates}")

if vi > vg:
  print("Inter venceu mais")
elif vg > vi:
  print("Gremio venceu mais")
else:
  print("Nao houve vencedor")