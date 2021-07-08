tempo = int(input())

horas = tempo // 3600
tempo -= horas * 3600

minutos = tempo // 60
tempo -= minutos * 60

print(f"{horas}:{minutos}:{tempo}")