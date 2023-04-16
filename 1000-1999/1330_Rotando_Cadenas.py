n = input().split()
rotaciones = int(n[1])
frase = n[0]
p = (frase[:-1])                #preparamos la subcadena
u = frase[-1]                   #obtenemos la ultima letra
nuevo = frase                   # en caso de que sea 0 guardamos por defecto
for i in range(rotaciones):
    nuevo = u + p               #la nueva cadena sera la rotacion
    u = nuevo[-1]               #se actualizaran los datos
    p = nuevo[:-1]              #se recorrera segun el parametro
print(nuevo)