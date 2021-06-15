def calcGolpe(atk, defesa, level, bonus):
  b = bonus if level % 2 == 0 else 0
  return ((atk + defesa) / 2) + b

n = int(input())
for _ in range(n):
  bonus = int(input())
  AD, DD, LD = [int(x) for x in input().split()]
  golpeD = calcGolpe(AD, DD, LD, bonus)
  AG, DG, LG = [int(x) for x in input().split()]
  golpeG = calcGolpe(AG, DG, LG, bonus)

  print("Dabriel" if golpeD > golpeG else "Guarte" if golpeD < golpeG else "Empate")