import sys
if __name__ == "__main__":
    for line in sys.stdin:      #lectura hasta el fin de archivo
        mayor = 0
        l = input()
        l = l.split()
        for i in l:
            a = l.count(i)      #obtenemos la cantidad de repeticiones que tiene cada numero
            if(a>mayor):        #el mayor es el que buscamos
                mayor = a
        if(mayor > 0):
            print(mayor)