def sumar_digitos(x):
    return sum(int(d) for d in str(x))

def ordenar_por_quickSort(v):
    if len(v) <= 1:
        return v
    else:
        pivot = v[0]
        izq = [x for x in v[1:] if sumar_digitos(x) < sumar_digitos(pivot) or (sumar_digitos(x) == sumar_digitos(pivot) and x < pivot)]
        der = [x for x in v[1:] if sumar_digitos(x) > sumar_digitos(pivot) or (sumar_digitos(x) == sumar_digitos(pivot) and x >= pivot)]
        return ordenar_por_quickSort(izq) + [pivot] + ordenar_por_quickSort(der)

n = int(input())
v = [int(x) for x in input().split()]
r = ordenar_por_quickSort(v)
for i in range(len(r)):
    if i == len(r) - 1:
        print(r[i])
    else:
        print(r[i], end=" ")
