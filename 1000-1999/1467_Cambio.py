while True:
    try:
        entrada = input().split()  # dividir la entrada en una lista de cadenas
        n = int(entrada[0])
        v = list(map(int, entrada[1:n+1]))  # convertir los siguientes n números a enteros
        valor = int(entrada[n+1])
        num_monedas = 0
        for j in range(n-1, -1, -1):
            num_monedas += valor // v[j]
            valor = valor % v[j]
        if valor == 0:
            print(num_monedas)
        else:
            print(-1)
    except EOFError:
        break
