import sys
sys.stdout = open(sys.stdout.buffer.fileno(), 'w', encoding='utf8')

while True:
  try:
    m = int(input())
  except EOFError:
    break

  moedas = []
  for _ in range(m):
    moedas.append(int(input()))
  
  n = int(input())

  s = 0
  for i in range(0, n, n):
    s += moedas[::-1][i]
  
  primo = True
  if s == 1:
    primo = False
  else:
    for num in range(2, s):
      if s % num == 0:
        primo = False
        break
  
  if primo:
    print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
  else:
    print("Bad boy! I’ll hit you.")
