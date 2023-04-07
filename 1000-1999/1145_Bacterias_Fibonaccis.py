f = []
for i in range(0, 201):
    f.append(0)


def fibo(n):
    if f[n] != 0:
        return f[n]
    if n < 2:
        return n
    else:
        f[n] = fibo(n - 1) + fibo(n - 2)
        return f[n]


m = int(input())
for i in range(0, m):
    print(fibo(int(input())))