# Extraer subcadenas usando slicing (rebanado de cadenas sin usar listas).

cadena = "abcdefghij"

# Índices negativos (cuentan desde el final)
print(cadena[-3:])     # "hij" - últimos 3 caracteres
print(cadena[-5:-2])   # "fgh" - desde el 5º desde el final hasta el 2º desde el final

# Con paso negativo
print(cadena[7:2:-1])  # "hgfed" - desde posición 7 hasta 2 en reversa
print(cadena[::-2])    # "jhfdb" - toda la cadena invertida tomando cada 2