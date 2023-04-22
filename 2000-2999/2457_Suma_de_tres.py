t = int(input())  # número de casos de prueba

for _ in range(t):
    a, b, c = map(int, input().split()) 
    if a + b == c or a + c == b or b + c == a:  # verifica todas las combinaciones posibles
        print("SI")
    else:
        print("NO")
