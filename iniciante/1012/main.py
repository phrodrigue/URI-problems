a, b, c = [float(x) for x in input().split(' ')]

print(f"TRIANGULO: {(a * c) / 2:0.3f}")
print(f"CIRCULO: {3.14159 * (c ** 2):0.3f}")
print(f"TRAPEZIO: {(c * (a + b)) / 2:0.3f}")
print(f"QUADRADO: {b ** 2:0.3f}")
print(f"RETANGULO: {a * b:0.3f}")