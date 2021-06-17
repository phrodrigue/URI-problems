while True:
  try:
    n, q = list(map(int, input().split()))
  except EOFError:
    break
  
  notas = []
  for _ in range(n):
    notas.append(int(input()))
   
  notas.sort(reverse=True)
  for _ in range(q):
    p = int(input()) - 1
    print(notas[p])