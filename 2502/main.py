while True:
    cont = 0
    try:
        entrada = input()
    except:
        break
    c, n = entrada.split(' ')
    codUm = input()
    um = codUm.lower() + codUm.upper()
    codDois = input()
    dois = codDois.lower() + codDois.upper()
    
    while cont < int(n):
        frase = input()
        l = []
        novaFrase = ''
        for letra in frase:
            if letra in um:
                pos = um.index(letra)
                l.append(dois[pos])
            elif letra in dois:
                pos = dois.index(letra)
                l.append(um[pos])
            else:
                l.append(letra)
        print(''.join(l))
        cont += 1
    print()
  