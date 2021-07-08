t = 39

linha = "-" * t

saida = f"{linha}\n|{'decimal':^11}|{'octal':^9}|{'Hexadecimal':^15}|\n{linha}\n"

for i in range(16):
  saida += f"|    {i:>3}    |{oct(i)[2:]:>5}    |{hex(i)[2:].upper():>8}       |\n"

saida += linha

print(saida)