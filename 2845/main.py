#  TLE

def verificaCoprimos(daLista, a):
  coprimos = True

  for i in range(2, daLista + 1):
    if daLista % i == 0 and a % i == 0:
      coprimos = False
      break
  
  return coprimos

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