n = int(input())

for _ in range(n):
  i = int(input())
  resp = ""
  if i == 0:
    resp = "NULL"
  else:
    if i % 2 == 0:
      resp = "EVEN"
    else:
      resp = "ODD"
    
    if i > 0:
      resp += " POSITIVE"
    else:
      resp += " NEGATIVE"

  print(resp)