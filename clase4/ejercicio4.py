presion = int(input('Ingrese la presion: '))
hum = int(input('Ingrese la humedad: '))
if ((hum > 75) & (presion < 1000)):
    print('Va a llover')
else: print('No va a llover')


