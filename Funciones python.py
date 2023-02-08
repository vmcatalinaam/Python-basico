# FUNCIONES

# Funcion para saber si un numero es PAR o IMPAR 

def esPar(numero_):
    if numero_%2 == 0: #modulo %
        print('El numero es par')
    else:
        print('El numero es impar') 

numero_ = int(input('Dime un # para saber si es par o no : '))

esPar(numero_) # llamar funcion con el # ingresao


# Funcion para saber si un numero es PAR o IMPAR 

def esPar(numero_):
    if numero_%2 == 0: #modulo %
        #print('El numero es par')
        return True
    else:
        #print('El numero es impar') 
        False

numero_ = int(input('Dime un # para saber si es par o no : '))
resultado = esPar(numero_) # llamar funcion con el # ingresao
print(resultado)


# Funcion suma

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

num1 = int(input('Dime un # : '))
num2 = int(input('Dime otro # : '))

# llamda  a la funcion

resultado = suma(num1,num2)
print(f'la suma es igual a: {resultado}')

