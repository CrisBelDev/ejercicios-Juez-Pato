import math

def round2(n):
    return math.floor(n * 100 + 0.5) / 100

T = int(input())

for _ in range(T):
    cadena = input().lower()
    a = cadena.count("a")
    e = cadena.count("e")
    i = cadena.count("i")
    o = cadena.count("o")
    u = cadena.count("u")
    total = len(cadena) - cadena.count(" ")
    print("Caso {0}:".format(_ + 1))
    print("a=", "{0:.2f}".format(round2((a * 100) / total)))
    print("e=", "{0:.2f}".format(round2((e * 100) / total)))
    print("i=", "{0:.2f}".format(round2((i * 100) / total)))
    print("o=", "{0:.2f}".format(round2((o * 100) / total)))
    print("u=", "{0:.2f}".format(round2((u * 100) / total)))
