t = int(input())

for i in range(t):
    n = int(input())
    vector = list(map(int, input().split()))
    valores_unicos = set(vector) # crea un conjunto con elementos unicos
    for nota in valores_unicos:
        if vector.count(nota) == 1:
            print(vector.index(nota))
            break
