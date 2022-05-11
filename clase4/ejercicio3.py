acumulador = 0 
contador = 0
cantidad = eval(input('Ingrese la cantidad de numeros a calcular: '))
for i in range(cantidad):
    numero = eval(input('Ingrese numero a calcular: '))
    acumulador = acumulador + numero
    contador = contador + 1
if contador > 0:
    promedio = acumulador/contador
    print('El promedio es de: ', promedio)