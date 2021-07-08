op = input()
valores = []

for iL in range(12):
  for iC in range(12):
    x = float(input())
    if iL + iC < 11 and iL < iC:
      valores.append(x)


if op == "S":
  print(f"{sum(valores):0.1f}")
else:
  print(f"{sum(valores) / len(valores):0.1f}")
