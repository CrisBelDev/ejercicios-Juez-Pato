# Autor: crisbeldev

# Función para verificar si a es divisible por b o b es divisible por a
def verificar_divisibilidad(a, b):
    if a % b == 0:
        return f"{a} es divisible por {b}"
    elif b % a == 0:
        return f"{b} es divisible por {a}"
    else:
        return "-1"

# Lee la entrada estándar hasta el final del archivo
import sys
for linea in sys.stdin:
    a, b = map(int, linea.strip().split())
    # Verifica la divisibilidad de a y b y la imprime
    print(verificar_divisibilidad(a, b))
