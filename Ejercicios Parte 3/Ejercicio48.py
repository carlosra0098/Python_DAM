""" Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de
cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva
ahorrado cada mes."""

ahorro = 0
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

print("Ingresa tus depósitos mensuales:")

for mes in meses:  # Recorre directamente la lista
    deposito = float(input("Depósito en " + mes + ": €"))
    ahorro += deposito
    print("Ahorro acumulado: €",ahorro)

print("Ahorro total en el año: €",ahorro)