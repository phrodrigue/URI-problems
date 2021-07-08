c = 1
while True:
  try:
    n = int(input())
  except EOFError:
    break

  totNum = 1
  seq = ["0"]
  for i in range(1, n + 1):
    for _ in range(i):
      seq.append(str(i))

  strNum = "numeros" if len(seq) > 1 else "numero"
  print(f"Caso {c}: {len(seq)} " + strNum)
  print(" ".join(seq))
  print()
  c += 1