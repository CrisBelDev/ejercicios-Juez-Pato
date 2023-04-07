n = int(input())
pal = "UMSAICPC"
aux = ''
for i in range(n):
    x = input()
    for item in pal:
        if(x.find(item) != -1):
            index = x.find(item)
            x = x[0:index] + x[index+1:]
            aux = aux + item
    if aux == pal:
        print('ES POSIBLE')
    else:
        print('NO ES POSIBLE')
    aux = ''