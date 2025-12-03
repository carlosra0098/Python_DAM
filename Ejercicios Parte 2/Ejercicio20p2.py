""" Programa que dada una cantidad de euros que el usuario introduce por teclado (múltiplo de
5 €) mostrará los billetes de cada tipo que serán necesarios para alcanzar dicha cantidad
(utilizando billetes de 500, 200, 100, 50, 20, 10 y 5). Hay que indicar el mínimo de billetes posible.
Por ejemplo, si el usuario introduce 145 el programa indicará que será necesario 1 billete de 100
€, 2 billetes de 20 € y 1 billete de 5 € (no será válido por ejemplo 29 billetes de 5, que aunque
sume 145 € no es el mínimo número de billetes posible)."""

cantidad = int(input("Introduce cantidad (múltiplo de 5): "))
    
if cantidad % 5 != 0:
    print("Error: Debe ser múltiplo de 5 €")
elif cantidad < 0:
    print("Error: La cantidad debe ser positiva")
else:
    restante = cantidad
        
    print("Para", cantidad,"€ se necesitan:")
        
    # Billete de 500
    if restante >= 500:
        billetes_500 = restante // 500
        restante = restante % 500
        print(billetes_500, "billete(s) de 500 €")
        
    # Billete de 200
    if restante >= 200:
        billetes_200 = restante // 200
        restante = restante % 200
        print(billetes_200, "billete(s) de 200 €")
        
    # Billete de 100
    if restante >= 100:
        billetes_100 = restante // 100
        restante = restante % 100
        print(billetes_100, "billete(s) de 100 €")
        
    # Billete de 50
    if restante >= 50:
        billetes_50 = restante // 50
        restante = restante % 50
        print(billetes_50, "billete(s) de 50 €")
        
    # Billete de 20
    if restante >= 20:
        billetes_20 = restante // 20
        restante = restante % 20
        print(billetes_20, "billete(s) de 20 €")
        
    # Billete de 10
    if restante >= 10:
        billetes_10 = restante // 10
        restante = restante % 10
        print(billetes_10, "billete(s) de 10 €")
        
    # Billete de 5
    if restante >= 5:
        billetes_5 = restante // 5
        restante = restante % 5
        print(billetes_5, "billete(s) de 5 €")
        
    if restante == 0:
        print("¡Cantidad exacta!")