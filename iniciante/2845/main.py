def verificaCoprimos(a, b):
  maior = a if a > b else b
  menor = a if a < b else b
  resto = menor

  while True:
    mdc = resto
    resto = maior % menor
    if resto != 0:
      maior = menor
      menor = resto
    else:
      break
  
  if mdc == 1:
    return True
  else:
    return False


n = int(input())
nums = [int(x) for x in input().split()]
maior = max(nums)

while True:
  maior += 1
  coprimos = []
  for num in nums:
    coprimos.append(verificaCoprimos(num, maior))
  
  if not False in coprimos:
    print(maior)
    break