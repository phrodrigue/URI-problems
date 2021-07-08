# INCOMPLETO - TIME LIMIT EXCEEDED

while True:
  try:
    n = int(input())
  except EOFError:
    break

  ordem = [int(x) for x in input().split()]
  tempo = [int(x) for x in input().split()]

  totTempo = 0

  while True:
    mudou = False
    for i in range(n - 1):
      if ordem[i] > ordem[i + 1]:
        t = ordem[i]
        ordem[i] = ordem[i + 1]
        ordem[i + 1] = t

        t = tempo[i]
        tempo[i] = tempo[i + 1]
        tempo[i + 1] = t

        totTempo += tempo[i] + tempo[i + 1]

        mudou = True

    if not mudou:
      break

  print(totTempo)