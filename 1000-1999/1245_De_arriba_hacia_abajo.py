def imprimir_numeros(x, y):
    if x >= y:  # caso base, cuando x es mayor o igual a y
        print(x)
        return
    else:
        print(y)
        imprimir_numeros(x, y-1)  # llamada recursiva con el valor de y disminuido en uno

# Pedimos al usuario que ingrese los valores de X e Y
x , y = map(int,input().split())
if x > y :
    imprimir_numeros(y, x)
else: 
    imprimir_numeros(x, y)

# Llamamos a la función recursiva para imprimir los números desde el mayor hasta el menor
