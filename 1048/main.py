salario = float(input())

if 0 < salario <= 400.00:
  reajuste = 0.15
elif 400.00 < salario <= 800.00:
  reajuste = 0.12
elif 800.00 < salario <= 1200.00:
  reajuste = 0.1
elif 1200.00 < salario <= 2000.00:
  reajuste = 0.07
else:
  reajuste = 0.04

novoSalario = salario * (1 + reajuste)
print(f"Novo salario: {novoSalario:0.2f}\nReajuste ganho: {novoSalario - salario:0.2f}\nEm percentual: {reajuste * 100:.0f} %")