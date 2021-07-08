totDias = int(input())

anos = totDias // 365
totDias -= anos * 365

meses = totDias // 30
totDias -= meses * 30

print(anos, 'ano(s)')
print(meses, 'mes(es)')
print(totDias, 'dia(s)')