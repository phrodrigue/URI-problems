n = int(input())
t = [0,0,0]
s = [0,0,0]
for _ in range(n):
  jog = input()
  tentativas = [int(x) for x in input().split()]
  sucesso = [int(x) for x in input().split()]
  
  t = [x + y for (x, y) in zip(tentativas, t)]
  s = [x + y for (x, y) in zip(sucesso, s)]
  
print(f"Pontos de Saque: {s[0] / t[0] * 100:0.2f} %.\n\
Pontos de Bloqueio: {s[1] / t[1] * 100:0.2f} %.\n\
Pontos de Ataque: {s[2] / t[2] * 100:0.2f} %.")