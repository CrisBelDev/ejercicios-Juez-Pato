import sys
if __name__ == "__main__":
    for num in sys.stdin:
        i = 0               #impares
        p = 0               #pares
        sw = True           #swap
        for dig in num:
            if dig == '\n': #al final de la cadena que se leyo esta un salto es para eso
                continue
            if sw:
                i += int(dig)
                sw = False
            else:
                p += int(dig)
                sw = True
        if i == p:
            print("SI")
        else:
            print("NO")