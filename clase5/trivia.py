import random


mundiales = (
        { 'anio': 1930, 'sede': 'Uruguay', 'campeon': 'Uruguay'},
        { 'anio': 1934, 'sede': 'Italia', 'campeon': 'Italia'},
        { 'anio': 1938, 'sede': 'Francia', 'campeon': 'Italia'},
        { 'anio': 1950, 'sede': 'Brasil', 'campeon': 'Uruguay'},
        { 'anio': 1954, 'sede': 'Suiza', 'campeon': 'Alemania'},
        { 'anio': 1958, 'sede': 'Suecia', 'campeon': 'Brasil'},
        { 'anio': 1962, 'sede': 'Chile', 'campeon': 'Brasil'},
        { 'anio': 1966, 'sede': 'Inglaterra', 'campeon': 'Inglaterra'},
        { 'anio': 1970, 'sede': 'México', 'campeon': 'Brasil'},
        { 'anio': 1974, 'sede': 'Alemania', 'campeon': 'Alemania'},
        { 'anio': 1978, 'sede': 'Argentina', 'campeon': 'Argentina'},
        { 'anio': 1982, 'sede': 'España', 'campeon': 'Italia'},
        { 'anio': 1986, 'sede': 'México', 'campeon': 'Argentina'},
        { 'anio': 1990, 'sede': 'Italia', 'campeon': 'Alemania'},
        { 'anio': 1994, 'sede': 'Estados Unidos', 'campeon': 'Brasil'},
        { 'anio': 1998, 'sede': 'Francia', 'campeon': 'Francia'},
        { 'anio': 2002, 'sede': 'Corea / Japón', 'campeon': 'Brasil'},
        { 'anio': 2006, 'sede': 'Alemania', 'campeon': 'Italia'},
        { 'anio': 2010, 'sede': 'Sudáfrica', 'campeon': 'España'},
        { 'anio': 2014, 'sede': 'Brasil', 'campeon': 'Alemania'},
        { 'anio': 2018, 'sede': 'Rusia', 'campeon': 'Francia'},
)


preguntas = ('anio', 'sede', 'campeon')
preguntar = random.choice(preguntas)
mundial = random.choice(mundiales)

print(preguntar)
print(mundial)



if preguntar == 'anio':
    print(f'Cuando fue el mundial en : {mundial["sede"]} que gano: {mundial["campeon"]}')
    rta = int(input('Ingrese su respuesta: '))
    if rta == mundial["anio"]:
        print('RESPUESTA CORRECTA!!! GANASTE EL AUTO!!!')
elif preguntar == 'campeon':
    print(f'Quien gano el mundial en : {mundial["sede"]} que se jugo en el anio: {mundial["anio"]}')
    rta = input('Ingrese su respuesta: ')
    if rta == mundial["anio"]:
        print('RESPUESTA CORRECTA!!! GANASTE EL AUTO!!!')
else:
    print(f'Donde fue el mundial del anio : {mundial["anio"]} que gano: {mundial["campeon"]}')
    rta = input('Ingrese su respuesta: ')
    if rta == mundial["anio"]:
        print('RESPUESTA CORRECTA!!! GANASTE EL AUTO!!!')

