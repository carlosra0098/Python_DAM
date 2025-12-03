""" Imprime una estrella de ocho puntas combinando líneas verticales,
horizontales y diagonales con asteriscos en una matriz de tamaño impar n x n (ej. 9x9).
*   *   *
 *  *  *
  * * *
*********
  * * *
 *  *  *
*   *   *"""

n = int(input("Introduce un número impar para el tamaño de la estrella (n): "))
for i in range(n):
    linea = ""
    for j in range(n):
        if i == n // 2 or j == n // 2 or i == j or i + j == n - 1:
            linea += "*"
        else:
            linea += " "
    print(linea)