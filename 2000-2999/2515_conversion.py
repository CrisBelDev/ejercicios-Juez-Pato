#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
# C = (F-32)*5/9
F = int(input())

C = (F-32)*5/9
print("{:.2f}".format(C))