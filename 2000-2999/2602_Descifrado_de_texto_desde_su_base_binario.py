# Descifrado de texto desde su base binario
def descifrar_valores(cifras):
    texto_descifrado = ""
    for cifra in cifras:
        binario = format(cifra, '08b')
        parte1 = binario[:4]
        parte2 = binario[4:]
        binario_intercambiado = parte2 + parte1
        valor_ascii = int(binario_intercambiado, 2)
        texto_descifrado += chr(valor_ascii)
    return texto_descifrado
K = int(input())
valores = list(map(int, input().split()))
resultado = descifrar_valores(valores)
print(resultado)