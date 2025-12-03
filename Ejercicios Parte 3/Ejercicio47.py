""" Escribe un programa que diga si un número introducido por teclado es o no primo. Un
número primo es aquel que sólo es divisible entre él mismo y la unidad. Nota: Es suficiente
probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número."""
numero = int(input("Introduce un número entero positivo: "))
if numero < 2:
    print(f"{numero} no es un número primo.")
    
else:
    es_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")