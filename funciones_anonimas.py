# FUNCIONES ANONIMAS

# FUNCION MAP 

lista1 = [23,456,32,1,78,11,23,56,23]

    #devuelve lista con el cuadrado

print(list(map((lambda valor: valor * valor),lista1))) #itera uno por uno para obtener el valor

# list = convierte en lista
# map = funcion que guarda
# lambda = funcion anonima

# FUNCION FILTER

# obtengo lista filtrada - retornar solo pares como ejemplo

print(list(filter((lambda valor: valor%2 == 0),lista1)))

# FUNCION REDUCE 

# no devulve lista, devulve valor

import functools

print(str(functools.reduce((lambda x,resultado: x + resultado),lista1)))
