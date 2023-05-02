# Problem H: Monedas
# Dennis se aburrió de estudiar y se puso a jugar con su coleccion de monedas, y las ordenó de la siguiente forma:
# solve.
import sys
t = int(input())
for i in range(t):
    x = int(input())
    elem = 1
    razon = 5
    s = 0
    for j in range(x):
        if j == (x-1):
            sys.stdout.write(str(elem))
        else:
            sys.stdout.write(str(elem)+ " ")
        elem = elem + razon
        razon = razon +4
    print()


