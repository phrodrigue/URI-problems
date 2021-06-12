l = [int(x) for x in input().split()]

hf = sum(l)
if hf >= 24:
  hf -= 24
elif hf < 0:
  hf += 24

print(hf)