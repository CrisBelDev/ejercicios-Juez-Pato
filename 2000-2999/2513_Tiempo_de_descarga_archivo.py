# Pedir al usuario el tamaño del archivo y la velocidad de descarga
tamano_archivo = int(input())
velocidad_descarga = int(input())

# Calcular el tiempo de descarga en segundos
tiempo_descarga = (tamano_archivo ) / velocidad_descarga

# Convertir el tiempo de descarga a minutos y segundos
segundos = tiempo_descarga
minutos = tiempo_descarga / 60
 

# Mostrar el resultado al usuario en el formato solicitado
print("{:.2f}".format(minutos ))
print("{:.2f}".format(segundos))
