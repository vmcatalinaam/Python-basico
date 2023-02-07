# Bucle for


# no se implemeta variable ni se incrementa
# ejemplo tabla de multiplicar:


tabla = int(input("indica la tabla que quiere calcular:  "))
print(f'Tabla del {tabla}')

# repetir mientras sea menor que 11, ya que la tabla va hasta el 10 toca uno mas

for contador in range(1,11): #final 11
    resultado = tabla * contador
    print(f'{tabla} por {contador} es igual a {resultado}')
print('fin del calculo')


# EJEMPLO: FOR LISTA

#recorre la lista y finaliza

nombres = ['Jose','Ana','Mario','Aleja','Vale']  #lista, array

for nombre in nombres:
    print(f'Hola {nombre}')
print('Fin de lista')


# MOSTRAR 100 numeros

for numero in range (0,100):
    result = numero +1
    print(f'lista de numeros : {result}')