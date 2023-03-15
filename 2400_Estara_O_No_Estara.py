cadena = input()
palabras = cadena.split()
palabras_con_o = []
for palabra in palabras:
    if "o" in palabra:
        palabras_con_o.append(palabra)

for palabra in palabras_con_o:
    if "," in palabra:
        palabra = palabra.replace(",", "")
    print(palabra)