import math

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(input())
raiz = int(math.sqrt(n))
contador = 0
s = 0

for _ in range(raiz+1):
    if s + factorial(raiz) <= n:
        s = s + (factorial(raiz))
        contador +=1
    else:
        raiz = raiz - 1
print(contador)
