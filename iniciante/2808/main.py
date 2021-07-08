col = ["a", "b", "c", "d", "e", "f", "g", "h"]

orig, dest = input().split()

col_orig = col.index(orig[0]) + 1
lin_orig = int(orig[1])

col_dest = col.index(dest[0]) + 1
lin_dest = int(dest[1])


if abs(col_orig - col_dest) == 2 and abs(lin_orig - lin_dest) == 1 or \
  abs(col_orig - col_dest) == 1 and abs(lin_orig - lin_dest) == 2:
  print("VALIDO")
else:
  print("INVALIDO")
