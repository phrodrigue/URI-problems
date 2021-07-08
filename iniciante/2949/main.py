especies = {
  "X": {"nome": "Hobbit", "tot": 0},
  "H": {"nome": "Humano", "tot": 0},
  "E": {"nome": "Elfo", "tot": 0},
  "A": {"nome": "Anao", "tot": 0},
  "M": {"nome": "Mago", "tot": 0},
}

n = int(input())

for _ in range(n):
  nome, esp = input().split()
  especies[esp]["tot"] += 1

for especie in especies:
  print(f"{especies[especie]['tot']} {especies[especie]['nome']}(s)")