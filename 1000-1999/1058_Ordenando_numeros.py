T = int(input())
for _ in range(T):
    n = input()
    lista = list(map(int , input().split()))
    lista.sort()
    print(*lista)