
def carrera():
    nombre = input('Ingrese el nombre del ciclista o 0 para finalizar: ')
    nombres = []
    tiempos = []
    acum = 0
    while nombre != str(0):
        nombres.append(nombre)
        tiempo = int(input('Ingrese el tiempo en minutos: '))
        if tiempo > 0:
            tiempos.append(tiempo)
        else:
            while tiempo <= 0:
                tiempo = int(input('Ingrese un tiempo valido en minutos: '))
            tiempos.append(tiempo)

        nombre = input('Ingrese el nombre del ciclista o 0 para finalizar: ')

    wintime = min(tiempos)
    wintimeind = tiempos.index(min(tiempos))
    ganador = nombres[wintimeind]

    print(f'El ganador es {ganador} con un tiempo de {wintime} minutos')

    record = int(input('Ingrese el tiempo récord: '))
    if wintime < record:
        print('El ganador estableció un nuevo récord de pista')

    for tiempo in tiempos:
        acum = acum + tiempo

    cantiempo = len(tiempos)
    promediotiempo = acum / cantiempo

    print(f'El tiempo promedio de la carrera es {int(promediotiempo)}')


carrera()
