import Paquetes.llamado_funcion

print(Paquetes.llamado_funcion.esPar(25)) #aqui llammamos la funcion de mi archivo alojado en paquete
print(Paquetes.llamado_funcion.esPar(20))


print(Paquetes.llamado_funcion.suma(20,10)) #de funcion suma guardada


# Otra forma de llamr paquetes
from Paquetes.llamado_funcion import * # * = todo o suma

print(esPar(50))
print(suma(10,10))