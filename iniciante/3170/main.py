b = int(input())
g = int(input())

totB = g // 2
dif = totB - b
saida = f"Faltam {dif} bolinha(s)" if dif > 0 else "Amelia tem todas bolinhas!"
print(saida)