n = int(input())
 
for i in range(n):
    tam = int(input())
    lista = list(map(int, input().split()))
    lista.sort()
    minimo = 100000000000000000000000
    for i in range(1,tam):
        a = lista[0:i]
        b = lista[i:tam]
        menor = max(a)-min(b)
        menor = abs(menor)
        if menor < minimo:
            minimo = menor
    print(f"{minimo}")