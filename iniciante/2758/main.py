import struct

um, dois = list(map(float, input().split()))
tres, quatro = list(map(float, input().split()))

um = struct.unpack('f', struct.pack('f', um))[0]
dois = struct.unpack('f', struct.pack('f', dois))[0]

saida = f"A = {um:6f}, B = {dois:6f}\nC = {tres:6f}, D = {quatro:6f}\n\
A = {um:0.1f}, B = {dois:0.1f}\nC = {tres:0.1f}, D = {quatro:0.1f}\n\
A = {um:0.2f}, B = {dois:0.2f}\nC = {tres:0.2f}, D = {quatro:0.2f}\n\
A = {um:0.3f}, B = {dois:0.3f}\nC = {tres:0.3f}, D = {quatro:0.3f}\n\
A = {um:0.3E}, B = {dois:0.3E}\nC = {tres:0.3E}, D = {quatro:0.3E}\n\
A = {um:.0f}, B = {dois:.0f}\nC = {tres:.0f}, D = {quatro:.0f}\n"
print(saida)