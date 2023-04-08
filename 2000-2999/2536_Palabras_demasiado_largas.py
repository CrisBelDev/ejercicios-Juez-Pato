T = int(input())
for i in range(T):
    cadena = input()
    longitud = len(cadena)
    if longitud <10:
        print(cadena)
    else:
        res = cadena[0]+str(longitud-2)+cadena[-1]
        print(res)