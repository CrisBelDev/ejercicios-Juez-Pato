t = int(input())

for i in range(t):
    cadena = input()
    horas, minutos = map(int, cadena.split(":"))
    segundos = (horas * 3600) + (minutos * 60)

    segundosFalsos = (horas*60) + (minutos)
    segundos = segundos - segundosFalsos

    horas = segundos // 3600
    segundos = segundos - (horas*3600)

    minutos = segundos // 60
    segundos = segundos - (minutos * 60)

    print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")