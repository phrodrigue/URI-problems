hi, mi, hf, mf = [int(x) for x in input().split()]

if hi > hf:
    durH = (24 - hi) + hf
elif hi < hf:
    durH = hf - hi
elif mi < mf:
    durH = 0
else:
    durH = 24

if mi > mf:
    durMin = (60 - mi) + mf
    durH -= 1
else:
    durMin = mf - mi
    
print(f'O JOGO DUROU {durH} HORA(S) E {durMin} MINUTO(S)')