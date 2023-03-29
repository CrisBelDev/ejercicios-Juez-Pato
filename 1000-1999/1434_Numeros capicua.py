def es_capicua(array):
    if len(array) <= 1:
        return True
    else:
        if array[0] == array[-1]:
            return es_capicua(array[1:-1])
        else:
            return False


numeros = input()

if es_capicua(numeros):
    print("S")
else:
    print("N")

