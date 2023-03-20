
from math import gcd
from random import randint
import math
import time

def f(x, c, n):
    return (x ** 2 + c) % n

def pollards(n):  ##returns factor, count
    x = 2
    c = 1
    y = f(x, c, n)
    d = 1
    counter = 0

    found = False
    while not found:
        x = f(x, c, n)
        y = f(f(y, c, n), c, n)
        d = gcd(abs(x - y), n)
        counter += 1

        if (d != 1 and d != n):
            found = True

        if (counter > 100000):
            return (-1, -1)
    print("N = %s factor = %s raizFactor = %s pasos = %s" % (n, d, round(pow(d,0.5),2), counter))

def brent(N):
    if N % 2 == 0:
        return 2
    step = 0
    y, c, m = randint(1, N - 1), randint(1, N - 1), randint(1, N - 1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = ((y**2) % N + c) % N
        k = 0
        while (k < r and g == 1):
            ys = y
            for i in range(min(m, r - k)):
                y = ((y**2) % N + c) % N
                q = q * (abs(x - y)) % N
            g = gcd(q, N)
            step+=1
            k = k + m
        r = r * 2
    if g == N:
        while True:
            ys = ((ys * ys) % N + c) % N
            g = gcd(abs(x - ys), N)
            step += 1
            if g > 1:
                break
    print("N = %s factor = %s raizFactor = %s pasos = %s" % (N, g, round(pow(g,0.5),2), step))

    return g
#---------------------
# halim
primos = []
def criba(n):

    global primos
    es_primo = [True] * (n + 1)
    es_primo[0] = es_primo[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if es_primo[i]:
            for j in range(i * i, n + 1, i):
                es_primo[j] = False

    for i in range(2, n + 1):
        if es_primo[i]:
            primos.append(i)


def factores_primos(N):
    global primos
    factores = []
    i = 0
    PF = primos[i]
    while N != 1 and PF * PF <= N:
        while N % PF == 0:
            N = N // PF
            factores.append(PF)
        i += 1
        PF = primos[i]
    if N != 1:
        factores.append(N)
    return factores


def factoHalim (n):
    try:

        criba(n)
        print(factores_primos(n))
    except:
        print("El número es demasiado grande para ser factorizado por esta función")

#---------------------
# factores hecho por mi
def genera_factors(n):
    max_time = 1
    factors = []
    start_time = time.time()
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
        if time.time() - start_time > max_time:
            return []

    return factors
#---------------------
print ("Pollard's result")
start_time = time.time()
pollards(715)
pollards(714731)
pollards(104681 * 104681)
pollards(104717 * 104717)
pollards(104729 * 104729)
pollards(104729 * 104717)
print ("--------------------------")
time1 = time.time() - start_time
print("--- %s seconds ---" % (time.time() - start_time))

print ("Brent's result")
start_time = time.time()
brent(715)
brent(714731)
brent(104681 * 104681)
brent(104717 * 104717)
brent(104729 * 104729)
brent(104729 * 104717)
print ("--------------------------")
time2 = time.time() - start_time
print("--- %s seconds ---" % (time.time() - start_time))

print ("Halim result")
start_time = time.time()
factoHalim(714)
factoHalim(714732)
factoHalim(104681 * 104681)
factoHalim(104717 * 104717)
factoHalim(104729 * 104729)
factoHalim(104729 * 104717)
time3 = time.time() - start_time
print("--- %s seconds ---" % (time.time() - start_time))


print ("Factorial hecho por mi: result")
start_time = time.time()
print(genera_factors(714))
print(genera_factors(714732))
print(genera_factors(104681 * 104681))
print(genera_factors(104717 * 104717))
print(genera_factors(104729 * 104729))
print(genera_factors(104729 * 104717))
time4 = time.time() - start_time
print("--- %s seconds ---" % (time.time() - start_time))


print("------TIEMPOS--------")
print("tiempo Pollard:\t",time1)
print("tiempo Brent:\t",time2)
print("tiempo Halim:\t",time3)
print("tiempo Facto normal :\t",time4)
print("__________________________")

"""
"""
if time2 < time1:
    percent = (abs(time1 - time2))/time2
    print ("Brent es %s por ciento más rápido que Pollard" % (round((percent*100), 2)))
else:
    percent = (abs(time2 - time1))/time1
    print ("Pollard es %s por ciento más rápido que Brent" % (round((percent*100), 2)))
