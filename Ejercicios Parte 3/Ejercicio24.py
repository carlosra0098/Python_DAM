""" Escribe un programa que pida un nombre de usuario y una contraseña y si se ha
introducido "pepe" y "asdasd" se indica "Has entrado al sistema", sino se da un error."""

nombre = input("Introduce tu nombre de usuario: ")
contraseña = input("Introduce tu contraseña: ")

if nombre == "pepe" and contraseña == "asdasd":
    print("Has entrado al sistema")
else:
    print("Error, no eres el usuario correcto")