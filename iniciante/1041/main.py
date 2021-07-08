x, y = [float(x) for x in input().split(" ")]

if x > 0 and y > 0:
  res = "Q1"
elif x < 0 and y > 0:
  res = "Q2"
elif x < 0 and y < 0:
  res = "Q3"
elif x > 0 and y < 0:
  res = "Q4"
elif x == 0 and y != 0:
  res = "Eixo Y"
elif y == 0 and x != 0:
  res = "Eixo X"
else:
  res = "Origem"

print(res)
