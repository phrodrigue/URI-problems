n = int(input())

for i in range(n):
  t = input()
  rgb = [int(x) for x in input().split()]
  if t == "max":
    res = int(max(rgb))
  elif t == "min":
    res = int(min(rgb))
  elif t == "mean":
    res = int(sum(rgb) / 3)
  elif t == "eye":
    res = int(rgb[0] * 0.3 + rgb[1] * 0.59 + rgb[2] * 0.11)
  
  print(f"Caso #{i + 1}: {res}")