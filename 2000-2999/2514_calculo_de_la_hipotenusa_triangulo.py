import math
cateto_adyacente = int(input())
cateto_opuesto = int(input())
hipotenusa = math.sqrt(cateto_adyacente**2 + cateto_opuesto**2)
print("{:.2f}".format(hipotenusa))