n = int(input())

grupos = {
  "bonecos": {"horas": 8, "totHoras": 0},
  "arquitetos": {"horas": 4, "totHoras": 0},
  "musicos": {"horas": 6, "totHoras": 0},
  "desenhistas": {"horas": 12, "totHoras": 0},
}

tot = 0

for _ in range(n):
  nome, grupo, horas = input().split()
  grupos[grupo]["totHoras"] += int(horas)

for grupo in grupos:
  tot += grupos[grupo]["totHoras"] // grupos[grupo]["horas"]

print(tot)