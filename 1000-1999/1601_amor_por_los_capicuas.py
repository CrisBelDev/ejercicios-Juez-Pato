casos = int(input())
for i in range(casos):
    x =input()                  
    if x == x[::-1]:            #X[::-1] es la cadena invertida de x
        print('SI')
    else:
        print('NO')