import math


def factor_primo_mas_grande(num):
    divisor = 2
    while divisor <= math.sqrt(num):
        if num % divisor == 0:
            num = num // divisor
        else:
            divisor = siguiente_primo(divisor)
    return num

def siguiente_primo(num):
    # Si el número es 2, el siguiente primo es 3
    if num == 2:
        return 3
    # Si no, empezamos a buscar el siguiente número primo a partir de num+2
    else:
        num += 2
        while not es_primo(num):
            num += 2
        return num

def es_primo(num):
    if num == 2:
        return True
    # Si el número es divisible por 2, no es primo
    elif num % 2 == 0:
        return False
    # Si no, buscamos divisores impares hasta la raíz cuadrada del número
    else:
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                return False
        return True

# Lectura de la entrada
while True:
    try:
        n = int(input())
        # Llamamos a la función para obtener el factor primo más grande y lo imprimimos
        print(factor_primo_mas_grande(n))
    except:
        # Si ocurre una excepción al leer la entrada, asumimos que ya no hay más casos de prueba y salimos del ciclo
        break
