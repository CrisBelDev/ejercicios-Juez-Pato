def complejidad(vector:list):
    mapa = []
    for i in range(0,len(vector)):
        if vector[i].find('for')!=-1:
            mapa.append(1)
        elif vector[i].find('}')!=-1:
            mapa.append(0)
    
    orden = 0
    acumulador = 0
    for i in range(0,len(mapa)):
        if mapa[i] == 1:
            acumulador = acumulador+1
        else:
            acumulador= acumulador-1
        if acumulador>orden:
            orden = acumulador
        
    if orden == 0:
        print(f'O(1)')
    else:
        print(f'O(n^{orden})')


n = int(input())
for i in range(n):
    numElem = int(input())
    codigo = []
    for w in range(numElem):
        codigo.append(input())
    complejidad(codigo)  
