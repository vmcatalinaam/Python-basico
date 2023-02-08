
# FUNCIONES ANIDADAS

# Funcion suma

def calcular(num1,num2, operacion):

    def suma(num1, num2):
        return num1 + num2
    
    def resta(num1, num2):
        return  num1 - num2
    
    def multiplicacion(num1, num2):
        return num1 * num2
    
    def division(num1, num2):
        return num1 / num2
    
    if operacion == 'Suma':
        print(f'{num1} + {num2} es = {suma(num1,num2)}')

    elif operacion == 'Resta':
        print(f'{num1} - {num2} es = {resta(num1,num2)}')
    
    elif operacion == 'multiplicacion':
        print(f'{num1} * {num2} es = {multiplicacion(num1,num2)}')
    
    elif operacion == 'Division':
        print(f'{num1} / {num2} es = {division(num1,num2)}')
    
    return 'Resultado devuelto'



# num1 = int(input('Dime un # : '))
# num2 = int(input('Dime otro # : '))


# llamda  a la funcion
print(calcular(10, 4, 'Resta'))

