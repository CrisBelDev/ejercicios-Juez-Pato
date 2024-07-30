pal = input()
pal = pal.replace(' ', '')
palabra = ''.join([j for i,j in enumerate(pal) if j not in pal[:i]])
for item in palabra:
    cant = pal.count(item)
    print(item + ' '+ str(cant))