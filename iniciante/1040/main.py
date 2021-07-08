notas = input()
n1, n2, n3, n4 = [float(x) for x in notas.split(" ")]

media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

print(f'Media: {round(media, 1)}')

if media < 5:
    print('Aluno reprovado.')
elif media >=7:
    print('Aluno aprovado.')
else:
    print('Aluno em exame.')
    nExame = float(input())
    print(f'Nota do exame: {nExame}')
    mediaFinal = (media + nExame) / 2
    if mediaFinal >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {round(mediaFinal, 1)}')
