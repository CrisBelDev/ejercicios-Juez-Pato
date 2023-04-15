import math

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

t = int(input())
primos = set()

for _ in range(t):
    n = int(input())
    if es_primo(n):
        primos.add(n)

n = len(primos)
ordenados = sorted(primos)
for i in range(n):
    if i == n-1:
        print(ordenados[i])
    else:
        print(ordenados[i], end=" ")
