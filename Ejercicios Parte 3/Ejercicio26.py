""" Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:
• El exponente sea positivo, sólo tienes que imprimir la potencia.
• El exponente sea 0, el resultado es 1.
• El exponente sea negativo, el resultado es 1/potencia con el exponente positivo."""

base = int(input("Dime la base(número): "))
exponente = int(input("Dime el exponente(elevado): "))

if exponente > 0:
    potencia = base ** exponente
    print(potencia)
elif exponente == 0:
    print("El resultado es 1")
elif exponente < 0:
    potencia = base ** (exponente * (- 1))
    resultado = 1 / potencia
    print(resultado)