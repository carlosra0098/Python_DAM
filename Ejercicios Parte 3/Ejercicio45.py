""" Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior
es mayor que el superior lo tiene que volver a pedir. A continuación, se van introduciendo
números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes
informaciones:
• La suma de los números que están dentro del intervalo (intervalo abierto).
• Cuantos números están fuera del intervalo.
• He informa si hemos introducido algún número igual a los límites del intervalo."""
limite_inf = int(input("Dime el limite inferior: "))
limite_sup = int(input("Dime el limite superior: "))

while limite_inf>=limite_sup:
    print("el limite inferior no puede ser mayor que el superior, introduzcalo de nuevo")
    limite_inf = int(input("Dime el limite inferior: "))
    limite_sup = int(input("Dime el limite superior: "))

suma = 0
fuera = 0
limite = False

salida = 1
while salida != 0:
    salida = int(input("Dame un numero, para salir introduce el cero: "))
    
    if limite_inf < salida < limite_sup:
        suma += salida
    elif salida == limite_inf or salida == limite_sup:
        limite = True
    elif limite_sup < salida or limite_inf < salida:
        fuera +=1

print(f"La suma de los numeros dentro del limite es: {suma}")
print(f"Hay {fuera} numeros fuera de los límites")
if limite:
    print("Uno de los numeros ha coincidido con uno de los limites")
else:
    print("No ha coincidido ningun numero con el limite")