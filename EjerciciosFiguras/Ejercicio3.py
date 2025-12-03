""" Imprime una pirámide de altura n donde se alternan asteriscos y espacios, formando un patrón de huecos internos.

Figura para n=6:

     *
    * *
   *   *
  * * * *
 *       *
*********** """

altura = int(input("Dime la altura de la pirámide: "))

for i in range(1, altura + 1):
    espacios = altura - i

    if i == 1:
        print(" " * espacios + "*")
    elif i == (altura // 2) + 1:
        print(" " * (altura - i) + "* " * ((altura // 2) + 1))
    elif i == altura:
        print("*" * ((altura * 2) - 1))
    else:
        print(" " * espacios + "*" + " " * (2 * i - 3) + "*")