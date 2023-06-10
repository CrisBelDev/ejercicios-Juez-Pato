t = int(input())
for _ in range(t):
    d, w = map(float, input().split())
    longitud = d * w
    longitud_formateada = "{:.3f}".format(longitud)
    print(longitud_formateada)
