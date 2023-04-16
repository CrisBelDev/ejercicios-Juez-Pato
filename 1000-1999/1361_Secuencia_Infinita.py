def encontrar_indice(n):
    bajo = 0          # Inicializar la variable 'bajo' en 0
    alto = n          # Inicializar la variable 'alto' en n
    while bajo <= alto:   # Realizar una búsqueda binaria mientras 'bajo' sea menor o igual a 'alto'
        medio = (bajo + alto) // 2   # Calcular el índice medio de la búsqueda
        triangular_medio = (medio * (medio + 1)) // 2  # Calcular el número triangular correspondiente al índice medio
        print(triangular_medio, bajo) 
        if triangular_medio == n:   # Si el número triangular es igual a n, devolver el índice medio
            return medio
        elif triangular_medio < n:  # Si el número triangular es menor que n, actualizar 'bajo' para buscar en la mitad superior de la búsqueda
            bajo = medio + 1
        else:                       # Si el número triangular es mayor que n, actualizar 'alto' para buscar en la mitad inferior de la búsqueda
            alto = medio - 1
    # Si no se encontró un número triangular igual a n, entonces n es el siguiente número después del último número triangular en la secuencia.
    # Para calcular su índice, utilizar la fórmula n - ((bajo - 1) * bajo // 2).
    return n - ((bajo - 1) * bajo // 2)

n = int(input())
indice = encontrar_indice(n)
print(indice)
