t = 39

linha = "-" * t
meio = "|" + (" " * (t - 2)) + "|"

print(f"{linha}\n|{'x = 35':<37}|\n{meio}\n|{'x = 35':^37}|\n{meio}\n|{'x = 35':>37}|\n{linha}")