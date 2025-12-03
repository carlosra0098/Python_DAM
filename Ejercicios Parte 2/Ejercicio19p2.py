""" Programa donde el usuario "piensa" un número del 1 al 100 y el ordenador intenta
adivinarlo. Es decir, el ordenador irá proponiendo números una y otra vez hasta adivinarlo (el
usuario deberá indicarle al ordenador si es mayor, menor o igual al número que ha pensado)."""
import random

print("Piensa un número del 1 al 100")
numero = random.randint(1, 100)

print("Este es tu número: ", numero)
resultado = input("Introduce si el número es 'mayor', 'menor' o 'igual': ")

match resultado:
    case 'mayor':
        while resultado == 'mayor':
            numero += 1
            print("Este es tu número: ", numero)
            resultado = input("Introduce si el número es 'mayor' o 'igual': ")
        resultado = input("Lo adiviné")
    
    case 'menor':
        while resultado == 'menor':
            numero -= 1
            print("Este es tu número: ", numero)
            resultado = input("Introduce si el número es 'menor' o 'igual': ")
        resultado = input("Lo adiviné")
        
    case 'igual':
        resultado = input("Lo adiviné")
            
        