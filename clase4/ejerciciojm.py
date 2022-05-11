acu=0

resp = int(input('ingrese cantidad de numeros que desea promedia: '))

for i in range(resp):
    numero = int(input('ingrese el numero: '))
    acu=acu+numero
if(resp!=0):
    prom =  acu/resp
    print('El primedio es: ', prom)

