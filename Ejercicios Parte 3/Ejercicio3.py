# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa. 
import math

cateto1 = int(input("Dime el primer cateto: "))
cateto2 = int(input("Dime el segundo cateto: "))

hipotenusa = math.sqrt((cateto1 * cateto1 + cateto2 * cateto2))

print("La hipotenusa es: ", hipotenusa)