""" Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales. Mostramos las
Iniciales en Mayúsculas sí o sí."""

nombre = input("Dime tu nombre: ")
apellido1 = input("Dime tu primer apellido: ")
apellido2 = input("Dime tu segundo apellido: ")

iniciales = nombre[0].upper() + apellido1[0].upper() + apellido2[0].upper()

print(iniciales)