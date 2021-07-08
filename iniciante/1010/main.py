prod1, n1, vlr1 = [float(x) for x in input().split(" ")]
prod2, n2, vlr2 = [float(x) for x in input().split(" ")]

valorFinal = (n1 * vlr1) + (n2 * vlr2)

print(f"VALOR A PAGAR: R$ {valorFinal:0.2f}")