import sys

if __name__ == "__main__":
    for datos in sys.stdin:
        datos = datos.split()
        n = int(datos[0])
        k = int(datos[1])
        if(n%2==0):
            if k > n//2:
                print((k - (n // 2)) * 2)
            else:
                print((k * 2) - 1)
        else:
            if k > (n//2) + 1:
                print((k - (n // 2)-1) * 2)
            else:
                print((k*2)-1)
