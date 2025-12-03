""" Crea una aplicación que permita adivinar un número. La aplicación genera un número
aleatorio del 1 al 100. A continuación, va pidiendo números y va respondiendo si el número a
adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10
intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en
cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número que
había generado."""

import random
numero_aleatorio = random.randint(1, 100)
intentos = 10
intento_actual = 0

print("¡Bienvenido al juego de adivinar el número!")
while intento_actual < intentos:
    intento_actual += 1
    numero_usuario = int(input(f"Intento {intento_actual}/{intentos}: Introduce un número entre 1 y 100: "))
    
    if numero_usuario < numero_aleatorio:
        print("El número a adivinar es mayor.")
    elif numero_usuario > numero_aleatorio:
        print("El número a adivinar es menor.")
    else:
        print(f"¡Felicidades! Has adivinado el número {numero_aleatorio} en {intento_actual} intentos.")
        break
else:
    print(f"Lo siento, has agotado tus intentos. El número era {numero_aleatorio}.")