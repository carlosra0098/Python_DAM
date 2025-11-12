""" Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
incorrecto."""

usuario_real = "usuario1234"
contrasena_real = "contrasenasegura1234"
entrar = False
entrar2 = False

nombre = input("Dime tu usuario: ")
contrasena = input("Dime tu contraseña: ")

if nombre == usuario_real:
    print("Usuario correcto")
    entrar = True
else:
    print("Usuario incorrecto")
    
if contrasena == contrasena_real:
    print("Contraseña correcta")
    entrar2 = True
else:
    print("Contraseña incorrecta")

