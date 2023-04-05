def menor(a:int, b:int):
    if a<b:
        return a
    return b

resultados = []
n = int(input())

for i in range(0,n):
    telas = input()
    r = telas.count("r")
    a = telas.count("a")
    v = telas.count("v")
    min = menor(r,menor(a,v))
    resultados.append(min)

for r in resultados:
    print(r)