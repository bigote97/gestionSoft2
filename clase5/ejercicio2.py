from random import randint


random = []
pares = []
impares = []

for i in range(20):
    #Utilizo la funcion randint() para obtener un valor random entero
    numero = randint(0, 99)
    # Agrego el numero aleatorio a mi lista
    random.append(numero)

for numero in random:
    if (numero % 2) == 0:
        # Si el resto de la division por 2 es 0 entonces el numero es par
        pares.append(numero)
    else:
        # Si el resto de la division por 2 es distinto 0 entonces el numero es impar
        impares.append(numero)

random.sort()
pares.sort()
impares.reverse()


print('Los 20 numeros aleatorios son: ', random)
print('Los  numeros pares son: ', pares)
print('Los  numeros impares son: ', impares)