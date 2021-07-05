saida = ""
while True:
  try:
    n = int(input())
  except EOFError:
    break

  sec = n / 100
  intSec = int(sec)

  if sec - intSec > 0:
    intSec += 1

  saida += f"{intSec}\n"

print(saida[:-1])