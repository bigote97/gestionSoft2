from triangulo import Triangulo
#instanciar la clase triangulo (la inicializo)
#a primer triangulo le digo que va a ser un objeto de clase triangulo
while True:

    primerangulo = int(input("Ingrese el primer angulo: "))
    segundoangulo = int(input("Ingrese el segundo angulo: "))
    tercerangulo = int(input("Ingrese el tercer angulo: "))

    untriangulo=Triangulo(primerangulo, segundoangulo, tercerangulo)
    untriangulo.mostrar()
    if untriangulo.verifica():
        print("es un triangulo")
    else:
        print("no es un triangulo")
    print(untriangulo.tipo())
    print(untriangulo.angulo())
    
    pregunta = input("Quiere continuar con otro triangulo? 1 para si, o presione cualquier boton para finalizar: ")
    if not pregunta == "1":
        break