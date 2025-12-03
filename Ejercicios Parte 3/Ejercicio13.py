""" Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se
puede calcular?"""
import math

num = int(input("Dime un número: "))

raiz_cuadrada = math.sqrt(num)

raiz_cubica = math.cbrt(num)

print("Raíz cuadradaa: ", raiz_cuadrada,". Raíz cúbica: ", raiz_cubica)