s = input()
s += "1" if s.count("1") % 2 == 1 else "0"
print(s)