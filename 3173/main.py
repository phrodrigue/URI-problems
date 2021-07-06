# WRONG ANSWER

def verificaAno(At):
  d = At * n * 365
  dInt = int(d)
  
  totDias = dInt

  dias = totDias
  totDias -= 10
  ano = 2021

  while totDias > 365:
    totDias -= 365
    ano += 1
    
    if ano % 4 == 0:
      dias += 1

  mes = 1
  for m in meses:
    if totDias >= m:
      totDias -= m
      mes += 1
    else:
      break

  data = f"{ano:0>4}-{mes:0>2}-{totDias:0>2}"

  return [dias, data]


meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = int(input())
anoInicial = 2020

jupiter = 11.9
saturno = 29.6
dias_j, data_j = verificaAno(jupiter)
dias_s, data_s = verificaAno(saturno)


saida = f"Dias terrestres para Jupiter = {dias_j}\n\
Data terrestre para Jupiter: {data_j}\n\
Dias terrestres para Jupiter = {dias_s}\n\
Data terrestre para Jupiter: {data_s}"

print(saida)
