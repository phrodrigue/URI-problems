n = int(input())
c = int(input())
venceu = True

for _ in range(n - 1):
  if int(input()) > c:
    venceu = False
    break

print("S" if venceu else "N")