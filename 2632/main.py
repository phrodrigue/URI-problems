from math import sqrt, pow

def medirDistancia(x, y):
  return sqrt(pow(x - cx, 2) + pow(y - cy, 2))
  

magias = {
  "fire": {"dano": 200, "alcance": [20, 30, 50]},
  "water": {"dano": 300, "alcance": [10, 25, 40]},
  "earth": {"dano": 400, "alcance": [25, 55, 70]},
  "air": {"dano": 100, "alcance": [18, 38, 60]},
}

n = int(input())

for _ in range(n):
  w, h, x0, y0 = [int(x) for x in input().split()]
  magia, nivel, cx, cy = input().split()
  nivel = int(nivel)
  cx = int(cx)
  cy = int(cy)

  distancias = []

  if cx <= x0 and cy <= y0 or \
      cy <= y0 and cx >= x0 + w or \
      cx <= x0 and cy >= y0 + h or \
      cy >= y0 + h and cx >= x0 + w:
    distancias.append(medirDistancia(x0, y0)) # inf esq
    distancias.append(medirDistancia(x0 + w, y0)) # inf dir
    distancias.append(medirDistancia(x0, y0 + h)) # sup esq
    distancias.append(medirDistancia(x0 + w, y0 + h)) # sup dir

   
  elif cx >= x0 and cy <= y0 and cx <= x0 + w or \
      cx >= x0 and cy >= y0 + h and cx <= x0 + w:
    # mesmo X do centro do circulo
    distancias.append(medirDistancia(cx, y0)) # inf centro
    distancias.append(medirDistancia(cx, y0 + h)) # sup centro

  elif cx <= x0 and cy >= y0 and cy <= y0 + h or \
      cx >= x0 + w and cy >= y0 and cy <= y0 + h:
    # mesmo Y do centro do circulo
    distancias.append(medirDistancia(x0, cy)) # centro esq
    distancias.append(medirDistancia(x0 + w, cy)) # centro dir
  
  else:
    distancias.append(0)

  distancia = min(distancias)


  if magias[magia]["alcance"][nivel - 1] >= min(distancias):
    print(magias[magia]["dano"])
  else:
    print(0)