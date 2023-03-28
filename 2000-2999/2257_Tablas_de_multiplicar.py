a , b = map(int,input().split())
lista =[]
for i in range(b):
    res = a * (i+1) 
    lista.append(res)
print(*lista,"")