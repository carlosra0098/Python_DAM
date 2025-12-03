"""Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad de
números primos que queremos mostrar."""

# Pedir cuántos números primos mostrar
n = int(input("¿Cuántos números primos quieres mostrar? "))

print(f"\nLos primeros {n} números primos son:")

contador = 0  # Cuántos primos hemos encontrado
numero = 2    # Empezamos a buscar desde el 2 (el primer primo)

while contador < n:
    es_primo = True
    
    # Verificar si 'numero' es primo
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    
    # Si es primo, lo mostramos
    if es_primo:
        print(numero, end=" ")
        contador += 1
    
    numero += 1