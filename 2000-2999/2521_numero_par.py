a = int(input())
b = int(input())
c = int(input())

def es_par(numero):
    if numero & 1 == 0:
        return True
    else:
        return False

if es_par(a) or es_par(b)  or es_par(c) :
    print("Hay un numero par")
else:
    print("No hay numeros pares")