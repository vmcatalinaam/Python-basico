
# CADENAS DE TEXTO

# centrado

texto = 'Esto es texto de    ejemplo'

print('empieza con ', texto.startswith('Esto'))
print('termina con ', texto.endswith('Esto'))


# alinear 

print(texto.center(len(texto)+10,"-"))

#elimina espacios
print(texto.strip())

# sustituir, se debe guardar en variabl

textoajuste = texto.replace("Esto","This")
print(textoajuste)