vector = [" ","!","$","%","(",")","*"]
vectorIndex = ["%20","%21","%24","%25","%28","%29","%2a"]

palabra = input()
while palabra != "#":
    textoFinal = ''
    for item in palabra:
    #  print(item)
        if item in vector:
            textoFinal = textoFinal + vectorIndex[vector.index(item)]
        else:
            textoFinal = textoFinal + item
    print(textoFinal)
    palabra = input()