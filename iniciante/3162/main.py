from math import sqrt, pow

def medeDistancia(l1, l2):
  x1, y1, z1 = l1
  x2, y2, z2 = l2

  d = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2))
  res = 2 if d <= 20 else 1 if 20 < d <= 50 else 0
  return res

sinais = ["B", "M", "A"]

n = int(input())
naves = []

for i in range(n):
  naves.append(
    {
      "pontos": [int(x) for x in input().split()],
      "maisProx": 0
    }
  )

for i in range(n - 1):
  l1 = naves[i]["pontos"]

  temp = naves[i + 1:]

  for t in range(n - i - 1):
    l2 = temp[t]["pontos"]
    sinal = medeDistancia(l1, l2)
    
    if sinal > naves[i]["maisProx"]:
      naves[i]["maisProx"] = sinal
    
    if sinal > temp[t]["maisProx"]:
      naves[t + i + 1]["maisProx"] = sinal
    

saida = ""
for nave in naves:
  saida += sinais[nave["maisProx"]] + "\n"

print(saida[:-1])