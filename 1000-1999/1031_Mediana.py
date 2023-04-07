
"""
Autor: Cristian Abel
Fecha: 7 de abril de 2023

"""
def medianda(lista):
    lista.sort()
    n = len(lista)
    if n == 1:
        print(lista[0])
    elif n % 2 != 0 :
        mitad = n//2
        elem = lista[mitad]
        if elem > lista[mitad-1] and elem < lista[mitad+1]:
            print(elem)
        else:
            print("-1")
    else: 
        print("-1")



# multiples casos hasta fin de archivo
while True:
    try:
        n = input()
        lista = list(map(int ,input().split()))
        medianda(lista)
    except EOFError:
        break
