n = int(input())

vector = []
for i in range(n):
    lista = list(map(int,input().split()))
    vector.append(lista)

c = 0
for lista in vector:
    if lista.count(1) >=2:
        c += 1
print(c)

