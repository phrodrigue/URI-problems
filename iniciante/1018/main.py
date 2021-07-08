valor = int(input())

cedulas = [100, 50, 20, 10, 5, 2, 1]

print(valor)
for cedula in cedulas:
    totCedulas = valor // cedula
    valor -= totCedulas * cedula
    print(f"{totCedulas} nota(s) de R$ {cedula},00")
