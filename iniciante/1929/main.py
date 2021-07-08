l = list(map(lambda x: int(x), input().split()))
r = "N"
for n in range(4):
  temp = l[:]
  temp.pop(n)
  temp.sort()
  if temp[0] + temp[1] > temp[2]:
    r = "S"
    break
print(r)
