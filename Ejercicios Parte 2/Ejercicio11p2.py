""" Crea una aplicación que dibuje una escalera de asteriscos. Nosotros le pasamos la altura de
la escalera por teclado. Este es un ejemplo si insertaras un 5 de altura:
**
***
****
*****"""

asterisco = "*"

altura_asterisco = int(input("Dime la altura que quieres para la escalera de asteriscos: "))

for i in range(1, altura_asterisco + 1):
    print(asterisco * i)
    
""" FORMAS DE CÓMO LO HACE EL PROFESOR
altura = int(input("Introduce la altura de la escalera: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("ERROR: Eres muy tonto, solamente son válidos los números enteros)
else:
print("\nForma nº1)
for i in range(1, altura + 1):
    for j in range(1, i + 1):
        print("*", end = "")
    print()
    
print(\nForma nº2)
asterisco="*"
for i in range(1,altura+1):
    print(asterisco)
    asterisco=asterisco+"*"
        
print(\nForma nº3)
for i in range(1,altura+1):
    print("*"*i)"""