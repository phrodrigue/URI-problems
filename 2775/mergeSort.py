# OUTRO METODO
# INCOMPLETO - falta somar o tempo

def mergeSort(lista):
  if len(lista) > 1:
    half = len(lista) // 2
    firstHalf = lista[:half]
    secondHalf = lista[half:]

    mergeSort(firstHalf)
    mergeSort(secondHalf)

    i = j = k = 0
    
    while i < len(firstHalf) and j < len(secondHalf):
      if firstHalf[i] < secondHalf[j]:
        lista[k] = firstHalf[i]
        i += 1
      else:
        lista[k] = secondHalf[j]
        j += 1
      k += 1
    
    while i < len(firstHalf):
        lista[k] = firstHalf[i]
        i += 1
        k += 1
    while j < len(secondHalf):
        lista[k] = secondHalf[j]
        j += 1
        k += 1




while True:
  try:
    n = int(input())
  except EOFError:
    break

  ordem = [int(x) for x in input().split()]
  tempo = [int(x) for x in input().split()]
  print(ordem)
  mergeSort(ordem)
  print(ordem)