a, b, c = [float(x) for x in input().split(" ")]

delta = round(b ** 2 - 4 * a * c, 2)

if delta < 0 or a == 0:
  print("Impossivel calcular")
else:
  x1 = (- b + (delta ** (1 / 2))) / (2 * a)
  x2 = (- b - (delta ** (1 / 2))) / (2 * a)
  
  print(f'R1 = {x1:0.5f}')
  
  if x1 != x2:
    print(f'R2 = {x2:0.5f}')
    