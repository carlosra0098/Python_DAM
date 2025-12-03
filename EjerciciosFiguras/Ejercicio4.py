""" Imprime un cuadrado de lado n con bordes de asteriscos y las dos diagonales marcadas, dejando espacios en el resto.

Figura para n=7:

*******
* *   *
*  *  *
*   * *
*  *  *
* *   *
******* """

altura =  int(input("Dime la altura de la figura, debe ser un numero impar: "))

for i in range(altura):
    if i == 0 or i == altura - 1:
        print(altura * "*")
    elif i < altura // 2:
        print("*" + " " * i + "*" + " " * (altura - i -3) + "*")
    else:
        print("*" + " " * (altura - i - 1) + "*" + " " * (i - 2) + "*")