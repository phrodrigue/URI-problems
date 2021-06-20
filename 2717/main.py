n = int(input())
t1, t2 = [int(x) for x in input().split()]

if t1 + t2 <= n:
  print("Farei hoje!")
else:
  print("Deixa para amanha!")