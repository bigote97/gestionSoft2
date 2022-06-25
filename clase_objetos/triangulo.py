#class es una clase
class Triangulo:
    #def es un metodo o una funcion
    #init es el metodo iniciador de las clases
    def __init__(self, angulouno, angulodos, angulotres):
        #self hace refencia a si mismo, a la clase triangulo en este caso
        #angulouno, dos y tres son parametros de la funcion o el metodo init
        self.angulouno = angulouno
        self.angulodos = angulodos
        self.angulotres = angulotres

    def mostrar(self):
        print(self.angulouno)
        print(self.angulodos)
        print(self.angulotres)

    def verifica(self):
        sumar = (self.angulouno + self.angulodos + self.angulotres)
        if sumar == 180:
            return True
        else:
            return False
    
    def tipo(self):
        if self.verifica():
            if self.angulouno == self.angulodos == self.angulotres:
                return 'Equilatero'
            elif self.angulouno == self.angulodos or self.angulouno == self.angulotres or self.angulodos == self.angulotres:
                return 'Isosceles'
            else:
                return 'Escaleno'
        else:
            return 'No es triangulo'

    def angulo(self):
        if self.verifica():
            if self.angulouno == 90 or self.angulodos == 90 or self.angulotres == 90:
                return 'Recto'
            elif self.angulouno > 90 or self.angulodos > 90 or self.angulotres > 90:
                return 'Obtusángulo'
            else:
                return 'Acutángulo'
        else:
            return 'dejate de joder no es triangulo'