n = int(input())
for _ in range(n):
  h, m, e = list(map(lambda x: int(x), input().split()))
  evento = "abriu" if e else "fechou"
  print(f"{h:0>2}:{m:0>2} - A porta {evento}!")