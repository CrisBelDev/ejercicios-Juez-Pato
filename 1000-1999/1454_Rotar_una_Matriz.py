lista = input().split(" ")
dimension = int(lista[0])
grados = int(lista[1])

matriz = []
for i in range(0, dimension):
    matriz.append(input().split(" "))

iteraciones = int(grados/90)


for i in range(0, iteraciones):
    matriz_girada = []  
    contador = 0
    for i in range(0,dimension):
        nueva_fila = []
        for fila in matriz[::-1]:
            nueva_fila.append(fila[i])
        contador = contador + 1
        
        matriz_girada.append(nueva_fila)
    matriz = matriz_girada




for fila in matriz:
    strA = " ".join(fila)
    print(strA)