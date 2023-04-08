# Leemos el peso de la sandía
peso = int(input())

# Verificamos si el peso total de la sandía es par
if peso % 2 == 0:
    # Verificamos si se puede dividir en dos partes de peso par
    if peso > 2 and peso % 4 == 0:
        print("SI")
    else:
        print("NO")
else:
    print("NO")