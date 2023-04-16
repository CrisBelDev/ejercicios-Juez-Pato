import sys
f = []
for i in range(0, 100):
    f.append(0)


def fibo(n):
    if f[n] != 0:
        return f[n]
    if n < 2:
        return n
    else:
        f[n] = fibo(n - 1) + fibo(n - 2)
        return f[n]


if __name__ == '__main__':
    for n in sys.stdin:
        print(fibo(int(n)))