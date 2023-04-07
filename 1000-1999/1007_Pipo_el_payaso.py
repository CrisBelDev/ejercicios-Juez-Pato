def obtCantPref(n):     
    pre = []
    for i in n:
        pre.append(i[0])
    letra = []
    mayor = 0
    for i in pre:       
        if i in letra:  
            continue
        letra.append(i) 
        nu = pre.count(i)
        if nu > mayor:  
            mayor = nu
    return mayor        


casos = int(input())
for i in range(casos):
    jug = []
    num = int(input())
    cant = []
    mayor = 0
    for j in range(num):            
        frase = input().split()
        nu = obtCantPref(frase)     
        if nu > mayor:              
            mayor = nu
        cant.append(nu)             
    print("El ganador es "+str(cant.index(mayor)+1)) 