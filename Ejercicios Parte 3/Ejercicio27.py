""" Algoritmo que pida dos números 'nota' y 'edad' y un carácter 'sexo' y muestre el mensaje
'ACEPTADA' si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es
'F'. En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. Si no se
cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'."""

edad = int(input("Dime tu edad: "))
nota = int(input("Dime tu nota: "))
sexo = input("Dime tu sexo (F o M): ").upper()

if edad >= 18 and nota >= 5 and sexo == "F":
    print("Aceptada")
elif edad >= 18 and nota >= 5 and sexo == "M":
    print("Posible")
else:
    print("No aceptada")