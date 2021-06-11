def converte(strNum):
  return int(strNum)

a, b = list(map(converte, input().split()))
print(a if a >= b else b)