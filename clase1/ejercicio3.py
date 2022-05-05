acumulador = 0
entrada = int(input('Ingrese el precio del producto, o 0  para salir: '))

while entrada != 0:
    acumulador = acumulador + entrada
    entrada = int(input('Ingrese el precio del producto, o 0  para salir: '))
if acumulador >= 1000:
    total = acumulador - acumulador * 0.10
    descuento = acumulador * 0.10
    print("El total de la compra es de: ", total)
    print("El descuento de la compra es de: ", descuento)

else:
    total = acumulador
    print("El total de la compra es de: ", total)


