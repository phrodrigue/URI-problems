while True:
  M, N = list(map(lambda x: int(x), input().split()))
  menor = M if M < N else N
  maior = M if M > N else N

  if menor <= 0:
    break

  soma = 0
  for n in range(menor, maior + 1):
    soma += n
    print(n, end=" ")

  print(f"Sum={soma}")