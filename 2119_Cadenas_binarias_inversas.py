def min_operations(s):
    # Contar el número de subcadenas que no tienen un cero y un uno
    count = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1

    # Devolver la mitad redondeada hacia arriba del número de operaciones necesarias para hacer que la cadena se alterne
    # (ya que cada operación invertirá dos caracteres)
    return (count + 1) // 2


# Ejemplo de uso
t = int(input())
for i in range(t):
    n = input()
    cad = input()
    print(min_operations(cad))
