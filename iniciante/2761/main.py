import struct

entrada = input().split(maxsplit=3)

num = int(entrada[0])
fl = float(entrada[1])
carac = entrada[2]
frase = entrada[3]

fl = struct.unpack('f', struct.pack('f', fl))[0]

saida = f"{num}{fl:0.6f}{carac}{frase}\n"
saida += "%d\t%f\t%c\t%s\n"%(num, fl, carac, frase)
saida += "%10d%10.6f%10c%10s"%(num, fl, carac, frase)

print(saida)