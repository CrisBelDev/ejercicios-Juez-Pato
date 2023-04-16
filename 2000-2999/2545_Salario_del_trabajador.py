T = int(input())
for _ in range(T):
    horas , salario = map(int,input().split())
    if horas <= 40 :
        pago = horas * salario
    else:
        pago = 40 * salario + (horas - 40) * salario * 1.5
    print("{:.2f}".format(pago))
