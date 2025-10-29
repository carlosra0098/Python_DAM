print("Hola")
x = [1,2,3]
y = [num*2 for num in x]
print(y)

x = 10
print(x)
x = 15 #reasignación y se pone este
print(x)
y = 20

x = y = z = 10

nombre = "Juan"
# nombre completo = "Error" Este no sirve porque tiene espacio

def saludo():
    nombre_ana = "Ana"
    print(f"Hola, {nombre_ana}")
    
def saludo_global():
    print(f"Hola, {nombre}")
    global nombre_ana
    
x = 10
y = x*3-3**10-2+3

# x = 10
# y = (x*3-3)**(10-2)+3 Da otro resultado totalmente distinto

print("Los valores de x, y son: ", x, y)

{'nombre': 'Jose', 'edad': 30}

N = 10
type(N)

palabra = "Python"
print(palabra[0])
print(palabra[3])
print(palabra[-1])
print(palabra[-0])
print(palabra[-2])
print(palabra[-6])
print(palabra[0:2])
print(palabra[2:])
print(palabra[-2:])
print(palabra[:2])
print(palabra[:])
print(palabra[:2] + palabra[2:])

palabra = "Python"
palabra[0] = "N" #No deja porque es inmutable por ser un String

palabra = "Python"
palabra = "N" + palabra[1:]
print(palabra) #Este si sirve porque no estas reasignando el String porque como he dicho antes el String es inmutable

