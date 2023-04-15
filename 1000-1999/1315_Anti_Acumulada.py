def anticumulada():
    n = int(input())
    v = list(map(int, input().split()))
    r = [0] * n
    
    for i in range(n):
        if i == 0:
            r[i] = v[i]
        else:
            r[i] = v[i] - v[i-1]

    for i in range(n):
        print(r[i], end=' ')

anticumulada()
