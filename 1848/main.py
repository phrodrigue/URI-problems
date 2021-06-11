for _ in range(3):
  soma = 0
  while True:
    entrada = input()
    if entrada == "caw caw":
      print(soma)
      break
    
    b = entrada.replace("-", '0').replace("*", '1')
    soma += int(b, 2)
