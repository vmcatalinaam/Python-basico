# GENERADORES

# funcion DEVOLVER NUMEROS IMPARES


def impares():
    for numero in range(1,50,2):  # #de 1 a 49 de 2 en 2
        yield numero # generado para que cada que se llame a la funcion nos devuelva # dentro del rango.

generador = impares()
for numero in generador:
    print(numero)
print(generador)

# # funcion DEVOLVER NUMEROS IMPARES UNO A UNO

def impares():
    for numero in range(1,50,2):  # #de 1 a 49 de 2 en 2
        yield numero # generado para que cada que se llame a la funcion nos devuelva # dentro del rango.

generador = impares()
print( next(generador))
print( next(generador))
print( next(generador)) #Imprimer lo 3 primeros

# # funcion DEVOLVER NUMEROS IMPARES UNO A UNO con FOR

def impares():
    for numero in range(1,50,2):  # #de 1 a 49 de 2 en 2
        yield numero # generado para que cada que se llame a la funcion nos devuelva # dentro del rango.

generador = impares()
num_limite = 15

for numero in generador:
     print(numero)
print(generador)