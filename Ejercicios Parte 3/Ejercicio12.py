""" Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
Calcula y muestra la distancia entre ellos."""
# raiz cuadrada de ((x2 - x1^2) + (y2 - y1^2)
import math

x1 = int(input("Dime la primera coordenada: "))
y1 = int(input("Dime la segunda coordenada: "))
x2 = int(input("Dime la tercera coordenada: "))
y2 = int(input("Dime la cuarta coordenada: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 -y1) ** 2)

print("La distancia entre los dos puntos es: ", distancia)