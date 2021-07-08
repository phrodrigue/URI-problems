diaInicio = int(input().replace("Dia ", ""))
hi, mi, si = [int(x) for x in input().split(" : ")]
diaFim = int(input().replace("Dia ", ""))
hf, mf, sf = [int(x) for x in input().split(" : ")]

dias = diaFim - diaInicio
horas = hf - hi
minutos = mf - mi
segundos = sf - si

if segundos < 0:
  segundos = 60 + segundos
  minutos -= 1

if minutos < 0:
  minutos = 60 + minutos
  horas -= 1

if horas < 0:
  horas = 24 + horas
  dias -= 1

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")