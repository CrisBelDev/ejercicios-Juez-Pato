def sumar_digitos(num):
    s = 0
    while num > 0:
        dig = num % 10
        num = num // 10
        s += dig
    return s

def generar_serie(n):
    num = 35
    sw = True
    serie = []
    for i in range(n):
        if sw:
            serie.append(num)
            sw = False
        else:
            suma = sumar_digitos(num)
            serie.append(suma)
            sw = True
            num += suma
    return serie

# Lectura de la entrada
T = int(input())
for i in range(T):
    n = int(input())
    serie = generar_serie(n)
    # Impresión de la salida
    for j in range(n):
        if j == n - 1:
            print(serie[j])
        else:
            print(serie[j], end="  ")
