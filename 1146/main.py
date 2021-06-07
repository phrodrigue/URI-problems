while True:
  x = input()

  if x == "0":
    break
  
  res = ""
  for n in range(1, int(x) + 1):
    res += f"{n} "
  
  print(res[:-1])
