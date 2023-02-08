# CALCULADORA 

# funcion menu
def menu():
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('4. Salir')

    opcion = int(input('?____')) 
    return opcion

# funcion para solicitar datos

def solicitardatos():
    num1 = int(input('Ingrese primer numero: '))
    num2 = int(input('Ingrese segundo numero: '))

    if num2 == 0:
        print('El numero no puede ser 0 \n')
    num2 = int(input('Ingrese segundo numero nuevamente: '))

    return num1, num2 # se devuelven los 3 valores

# funcion operaciones

def operacion(operador, num1, num2):
    if operador == 'Suma':
        resultado = num1 + num2
    elif operador == 'Resta':
        resultado = num1 - num2
    elif operador == 'Multiplicacion':
        resultado = num1 * num2
    elif operador == 'Division':
        resultado = num1 / num2
    
    return resultado

# crear bucle para la llamada de las funciones

while True: # siempre verdadero hasta que demos opcion de salir
    opcion = menu()
    if opcion == 1:
        num1, num2 = solicitardatos()
        print(f'El resultado de {num1} + {num2} es = ')
        print(operacion('Suma', num1, num2))
    elif opcion == 2:
        num1, num2 = solicitardatos()
        print(f'El resultado de {num1} - {num2} es = ')
        print(operacion('Resta', num1, num2))
    elif opcion == 3:
        num1, num2 = solicitardatos()
        print(f'El resultado de {num1} * {num2} es = ')
        print(operacion('Multiplicacion', num1, num2))
    elif opcion == 4:
        num1, num2 = solicitardatos()
        print(f'El resultado de {num1} / {num2} es = ')
        print(operacion('Division', num1, num2))
    elif opcion == 0:
        break
    else:
        print('Inroduce una opción valida')
    print('\n')
print('Salimos')




            


