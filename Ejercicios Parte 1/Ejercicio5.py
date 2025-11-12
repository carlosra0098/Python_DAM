"""Escriba un programa que toma como dato de entrada un número que corresponde a la
longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la esfera
que corresponde con dicho radio."""
import math

print("Introduce el radio")
radio = input()
radio = int(radio)

diametro = radio * 2
longitud = diametro / 2
longitud_circunferencia = math.pi * diametro
area_circulo = 3.14 * radio**2
volumen_esfera = 4/3 * math.pi * radio**3

print(f"El diámetro es: {diametro:.2f}, La longitud es: {longitud:.2f}, La longitud de la circunferencia es: {longitud_circunferencia:.2f}, El área del círculo es: {area_circulo:.2f}, El volumen de la esfera es: {volumen_esfera:.2f} ")
