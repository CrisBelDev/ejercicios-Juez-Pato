def imprimir_numeros(x):
    if x <= 0:  # caso base, cuando x es mayor o igual a y
        print(x)
        return
    else:
        
        imprimir_numeros(x-1)  # llamada recursiva con el valor de y disminuido en uno
        print(x)
# Pedimos al usuario que ingrese los valores de X e Y
x = int(input())
imprimir_numeros(x)
