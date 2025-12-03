# Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower()).

# Texto de entrada
texto = "Hola Mundo"
resultado = ""

# Convertir a mayúsculas
for caracter in texto:
    if 'a' <= caracter <= 'z':
        # Restar 32 para convertir minúscula a mayúscula en ASCII
        resultado += chr(ord(caracter) - 32)
    else:
        resultado += caracter

print("Texto original:", texto)
print("En mayúsculas:", resultado)

# Texto de entrada
texto = "HOLA MUNDO"
resultado = ""

# Convertir a minúsculas
for caracter in texto:
    if 'A' <= caracter <= 'Z':
        # Sumar 32 para convertir mayúscula a minúscula en ASCII
        resultado += chr(ord(caracter) + 32)
    else:
        resultado += caracter

print("Texto original:", texto)
print("En minúsculas:", resultado)