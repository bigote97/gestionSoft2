import datetime
la_hora = datetime.datetime.now().strftime("%X")
la_fecha = datetime.datetime.now().strftime("%x")

x = [2, 'a', 9, 7, 'b'] # Lista, puede almacenar distintos tipos de variables, caracteristica clave: ES MUTABLE
z = (2, 'a', 9, 7, 'b') # Tupla, puede almacenar distintos tipos de variables, caracteristica clave: ES INMUTABLE
y = {'peru':'lima', 'chile':'santiago', 'bolivia':'la paz', 'uruguay':'montevideo'} # Diccionario, puede almacenar distintos tipos de variables, caracteristica clave: No tiene posiciones, tiene claves y valores
s = {2, 'a', 9, 7, 'b'} # Set, puede almacenar distintos tipos de variables, caracteristica clave: NO TIENEN ORDEN
#s = set(2, 'a', 9, 7, 'b') # Set, puede almacenar distintos tipos de variables, caracteristica clave: NO TIENEN ORDEN



print('La hora es: ', la_hora)
print('La fecha es: ', la_fecha)
print('Lista: ', x)
print('Tupla: ', z)
print('Diccionario: ', y)
print('Set: ', s)
print('Set: ', s)