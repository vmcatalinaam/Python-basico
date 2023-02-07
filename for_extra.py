

lista_colores = ['rojo','verde','gris','azul','morado','rosa']
mi_color = 'gris'

for color in lista_colores:
    print(color)
    if color == mi_color:
        print('Color encontrado')
        break # por si encuentra mi color
    else:
        print("El color indicado no esta en la lista")
else:
    print("He terminado de recorrer la lista")


rango_largo = range(1,10000)
print(rango_largo)

for numero in rango_largo:
    print(numero)
    if numero == 5:
        print('encontrado el # 5')
        break