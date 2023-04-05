n, i, j = map(int, input().split())
valores = list(map(int, input().split()))
resultado = valores[0:i]+valores[j:i-1:-1]+valores[j+1:len(valores)]
for i in resultado:
    print(i)