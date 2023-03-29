def generar_terminos(t):
    lista = []
    n = 10
    for i in range(40):
        modulo = n % t
        n = n // t
        lista.append(n)

        if modulo < t:
            n = modulo * 10
    return lista




def primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def print_number(n):
    if primo(n):
        lista = generar_terminos(n)
        cad = str(n) + ":"

        print(cad, *lista,"")
    else:
        print(str(n) + ": -1")


t = int(input())
for i in range(t):
    print_number(int(input()))


