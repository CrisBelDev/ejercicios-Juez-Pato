def es_palindromo_recursivo(array):
    """
    Determina si un array es un palíndromo de forma recursiva.
    
    Parameters:
    -----------
    array : list
        La lista que se quiere comprobar si es palíndromo.
        
    Returns:
    --------
    bool
        Devuelve True si el array es un palíndromo, y False en caso contrario.
    """
    # Caso base: la longitud del array es 0 o 1, lo que significa que es un palíndromo
    if len(array) <= 1:
        return True
    else:
        # Si el primer y último elemento del array son iguales, llamamos recursivamente a la función
        # con el array sin el primer y último elemento
        if array[0] == array[-1]:
            return es_palindromo_recursivo(array[1:-1])
        else:
            # Si el primer y último elemento del array no son iguales, entonces no es un palíndromo
            return False

# Solicitamos al usuario que ingrese un número y una lista de números
n = int(input())
numeros = list(map(int, input().split()))

# Llamamos a la función es_palindromo_recursivo con la lista de números
if es_palindromo_recursivo(numeros):
    # Si la función devuelve True, entonces la lista es un palíndromo
    print("SI")
else:
    # Si la función devuelve False, entonces la lista no es un palíndromo
    print("NO")

