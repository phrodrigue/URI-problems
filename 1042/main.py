list = [int(x) for x in input().split()]
origList = list[:]

list.sort()
for n in list:
  print(n)

print()

for n in origList:
  print(n)
