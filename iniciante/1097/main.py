jotas = [7, 6, 5]

for i in range(1, 10, 2):
  for j in jotas:
    print(f"I={i} J={j}")
  jotas = [x + 2 for x in jotas]
  #jotas = list(map(lambda x: x + 2, jotas))