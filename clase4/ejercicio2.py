acumulador = 1000
while acumulador > 0:
    pago = eval(input('Ingrese valor de la cuota a pagar: '))
    acumulador = acumulador - pago
    print('El total de la deuda es de: $', acumulador)
print('Deuda pagada.')