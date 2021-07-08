lista = [float(x) for x in input().split(" ")]
sortedList = lista[:]
sortedList.sort()

if sortedList[0] + sortedList[1] > sortedList[2]:
  print(f"Perimetro = {sum(lista):0.1f}")
else:
  area = ((lista[0] + lista[1]) * lista[2]) / 2
  print(f"Area = {area:0.1f}")
