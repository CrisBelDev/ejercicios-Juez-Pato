def min_operations(s):
    # Contar el número de subcadenas que no tienen un cero y un uno
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1

    # Devolver la mitad redondeada hacia arriba del número de operaciones necesarias para hacer que la cadena se alterne
    # (ya que cada operación invertirá dos caracteres)
    return (count + 1) // 2


# Leer el número de casos de prueba
t = int(input())

# Procesar cada caso de prueba
for i in range(t):
    # Leer la longitud de la cadena y la cadena en cada caso de prueba
    n = input()
    cad = input()
    
    # Llamar a la función min_operations para obtener la cantidad mínima de operaciones necesarias para hacer que la cadena se alterne
    result = min_operations(cad)
    
    # Imprimir el resultado para cada caso de prueba
    print(result)
