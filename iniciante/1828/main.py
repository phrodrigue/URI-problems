r = {
  "tesoura": {
    "vence": ["papel", "lagarto"],
    "perde": ["Spock", "pedra"]
  },
  "papel": {
    "vence": ["Spock", "pedra"],
    "perde": ["tesoura", "lagarto"]
  },
  "pedra": {
    "vence": ["tesoura", "lagarto"],
    "perde": ["papel", "Spock"]
  },
  "lagarto": {
    "vence": ["papel", "Spock"],
    "perde": ["tesoura", "pedra"]
  },
  "Spock": {
    "vence": ["pedra", "tesoura"],
    "perde": ["lagarto", "papel"]
  },
}

n = int(input())

for i in range(1, n + 1):
  sh, raj = input().split()
  jogSh = r[sh]
  if raj in jogSh["vence"]:
    res = "Bazinga!"
  elif raj in jogSh["perde"]:
    res = "Raj trapaceou!"
  else:
    res = "De novo!"
  
  print(f"Caso #{i}: {res}")