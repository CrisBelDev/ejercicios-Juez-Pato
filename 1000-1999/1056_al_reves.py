n = int(input())

for i in range(0, n):
    n = input()
    a = input()     
    a = a.split()   
    a.reverse()     #invierto el vector
    cad = ""
    for j in a:
        cad+=j+" "  #guardo en una cadena
    print(cad)      #imprimo