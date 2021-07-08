a = input()
b = input()
c = input()

saida = f"{a}{b}{c}\n\
{b}{c}{a}\n\
{c}{a}{b}\n\
{a[:10]}{b[:10]}{c[:10]}"

print(saida)