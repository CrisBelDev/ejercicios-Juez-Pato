# 1 pie = 12 pulgadas y 1 pulgada = 2.54 centímetros.
pulgada = 2.54
pie = 12*pulgada

E_pies = int(input())
E_pulgadas = int(input())

longitud_cm = E_pies*pie + E_pulgadas*pulgada
print("{:.2f}".format(longitud_cm))
