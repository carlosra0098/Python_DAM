""" Escriba un programa que lea un valor correspondiente a una distancia en millas marinas y 
escriba la distancia en metros. Sabiendo que una milla marina equivale a 1.852 metros."""

print("Dime las millas marinas que quieres calcular")
millas_marinas = input()
millas_marinas = int(millas_marinas)

metros = 1.852 * millas_marinas
print("Los metros son: ", metros)