acumulador = 0
while True:
    try:
        entrada = eval(input('Ingrese el precio del producto, o 0  para salir: '))
        break
    except:
        print('except')
        #entrada = eval(input('Ingrese el precio del producto, o 0  para salir: '))


while entrada != 0:
    acumulador = acumulador + entrada
    print('Subtotal de compra: ', acumulador)
    while True:
        try:
            entrada = eval(input('Ingrese el precio del producto, o 0  para salir: '))
            break
        except:
            print('except')
            # entrada = eval(input('Ingrese el precio del producto, o 0  para salir: '))
if acumulador >= 1000:
    total = acumulador - acumulador * 0.10
    descuento = acumulador * 0.10
    print("El total de la compra es de: ", total)
    print("El descuento de la compra es de: ", descuento)

else:
    total = acumulador
    print("El total de la compra es de: ", total)


