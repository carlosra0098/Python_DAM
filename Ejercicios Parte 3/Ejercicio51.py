"""Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 euros, el
segundo 20 euros, el tercero 40 euros y así sucesivamente. Realizar un algoritmo para
determinar cuánto debe pagar mensualmente y el total de lo que pagó después de los 20 meses."""
print("=== CÁLCULO DE PAGOS GEOMÉTRICOS ===")

print("=== PLAN DE PAGOS DUPLICADOS MENSUALMENTE ===")

pago_mes = 10  
total_pagado = 0

print("\nPagos mensuales:")
for mes in range(1, 21):
    print("Mes " ,mes, ": €", pago_mes)
    total_pagado += pago_mes
    pago_mes *= 2  # Se duplica para el próximo mes

print("Total pagado después de 20 meses: €" ,total_pagado)