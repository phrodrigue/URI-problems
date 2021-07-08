cobaias = {
  "R": 0,
  "S": 0,
  "C": 0,
}

n = int(input())

for _ in range(n):
  num, tipo = input().split()
  cobaias[tipo] += int(num)

total = cobaias['R'] + cobaias['S'] + cobaias['C']
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {cobaias['C']}")
print(f"Total de ratos: {cobaias['R']}")
print(f"Total de sapos: {cobaias['S']}")
print(f"Percentual de coelhos: {cobaias['C'] * 100 / total:0.2f} %")
print(f"Percentual de ratos: {cobaias['R'] * 100 / total:0.2f} %")
print(f"Percentual de sapos: {cobaias['S'] * 100 / total:0.2f} %")
