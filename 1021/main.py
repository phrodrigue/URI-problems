notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

vlr = round(float(input()) * 100)

print("NOTAS:")
for n in notas:
  n = int(n * 100)
  tot = vlr // n
  vlr -= tot * n
  print(f'{tot:.0f} nota(s) de R$ {n / 100:0.2f}')
  
print("MOEDAS:")
for n in moedas:
  n = int(n * 100)
  tot = vlr // n
  vlr -= tot * n
  print(f'{tot:.0f} moeda(s) de R$ {n / 100:0.2f}')