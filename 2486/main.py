alimentos = {
  "suco de laranja": 120,
  "morango fresco": 85,
  "mamao": 85,
  "goiaba vermelha": 70,
  "manga": 56,
  "laranja": 50,
  "brocolis": 34,
}

while True:
  n = int(input())
  if n == 0:
    break
  
  tot = 0
  for _ in range(n):
    entrada = input().split()
    tot += int(entrada[0]) * alimentos[" ".join(entrada[1:])]
  
  if tot > 130:
    print(f"Menos {tot - 130} mg")
  elif tot < 110:
    print(f"Mais {110 - tot} mg")
  else:
    print(tot, "mg")
  
