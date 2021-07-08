n = int(input())
emCasa = noTrabalho = totCasa = totTrab = 0

for _ in range(n):
  chuvaNaIda, chuvaNaVolta = [False if x == "sol" else True for x in input().split()]

  if chuvaNaIda:
    if not emCasa:
      emCasa = 1
      totCasa += 1
    
    emCasa -= 1
    noTrabalho += 1
  
  if chuvaNaVolta:
    if not noTrabalho:
      noTrabalho = 1
      totTrab += 1
    
    noTrabalho -= 1
    emCasa += 1

print(totCasa, totTrab)