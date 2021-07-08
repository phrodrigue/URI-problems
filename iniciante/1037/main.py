n = float(input())

if 0 <= n <= 25:
  interv = "[0,25]"
elif 25 < n <= 50:
  interv = "(25,50]"
elif 50 < n <= 75:
  interv = "(50,75]"
elif 75 < n <= 100:
  interv = "(75,100]"
else:
  interv = False

if interv:
  print(f"Intervalo {interv}")
else:
  print("Fora de intervalo")
