""" Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un
dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta
al resultado obtenido.
Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el
mensaje: "ERROR: número incorrecto."."""

dado = int(input("Dime que cara ha salido del dado(1 al 6): "))

if dado < 1 or dado > 6:
    print("ERROR: número incorrecto.")
else:

    if dado == 1:
        resultado = 6
    elif dado == 2:
        resultado = 5
    elif dado == 3:
        resultado = 4
    elif dado == 4:
        resultado = 3
    elif dado == 5:
        resultado = 2
    else: 
        resultado = 1

    if resultado == 1:
        texto = "UNO"
    elif resultado == 2:
        texto = "DOS"
    elif resultado == 3:
        texto = "TRES"
    elif resultado == 4:
        texto = "CUATRO"
    elif resultado == 5:
        texto = "CINCO"
    else: 
        texto = "SEIS"

    print("Cara opuesta:", texto)