n = int(input())
saida = "Minimum note not reached"
maiorNota = 0
for _ in range(n):
  aluno, nota = input().split()
  nota = float(nota)
  if nota > maiorNota and nota >= 8.0:
    maiorNota = nota
    saida = aluno

print(saida)