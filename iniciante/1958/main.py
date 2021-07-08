entrada = input()
n = float(entrada)
nc = f"{n:.4e}".upper()
r = nc if entrada[0] == "-" else "+" + nc
print(r)