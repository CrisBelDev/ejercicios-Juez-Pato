def es_hombre(usuario):
    genero = eliminar_repetidos(usuario)
    if len(genero)% 2 == 0:
        print("CHATEA CON ELLA!")
    else:
        print("IGNORARLO!")

def eliminar_repetidos(cadena):
    nueva_cadena = ""
    for c in cadena:
        if c not in nueva_cadena:
            nueva_cadena += c
    return nueva_cadena

usuario = input()
es_hombre(usuario)

