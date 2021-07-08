from math import pow, sqrt
while True:
  try:
    Xf, Yf, Xi, Yi, Vi, R1, R2 = [int(x) for x in input().split()]
  except EOFError:
    break

  D1 = sqrt(pow(Xi - Xf, 2) + pow(Yi - Yf, 2)) + (Vi * 1.5)
  D2 = R1 + R2
  dif = D2 - D1
  print("Y" if dif >= 0 else "N")