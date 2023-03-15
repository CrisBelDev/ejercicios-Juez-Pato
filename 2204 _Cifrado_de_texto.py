while True:
    try:
        cadena = input().strip()
    except:
        break

    cifrado = []
    for caracter in cadena:
        binario = bin(ord(caracter))[2:].zfill(8)
        cifra_binario = binario[4:] + binario[:4]
        cifra_decimal = int(cifra_binario, 2)
        cifrado.append(cifra_decimal)

    print(*cifrado)