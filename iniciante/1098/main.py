lj = [1,2,3]
i = 0
incremento = 0.2

while i <= 2:
  for j in lj:
    i = round(i, 1)
    j = round(j, 1)

    if round(i - int(i), 1) == 0.0:
      print(f"I={int(i)} J={int(j)}")
    else:
      print(f"I={i:.1f} J={j:.1f}")
  # lj = list(map(lambda x: x + 0.2, lj))
  lj = [x + incremento for x in lj]
  i += incremento
