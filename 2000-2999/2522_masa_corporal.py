peso = int(input())
altura = float(input())
indice_masa_c = round(peso / altura**2 , 2)
print(indice_masa_c)

if indice_masa_c < 18.5:
    print("Bajo peso")
if indice_masa_c >18.5 and indice_masa_c< 24.9:
    print("Peso normal")
if indice_masa_c >25 and indice_masa_c< 29.9:
    print("Sobrepeso")
if indice_masa_c >30:
    print("Obesidad")