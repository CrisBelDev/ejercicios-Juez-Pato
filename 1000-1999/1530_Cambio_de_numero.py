n = int(input())
for i in range(n):
    c = input()
    l = len(c)
    aux = '0'
    for j in range(l):
        if(c[j] != '0' and c[j] != '1' and c[j] != '4' and c[j] != '6' and c[j] != '8' and c[j] != '9'):
            aux=aux+c[j]
    print(int(aux.strip()))