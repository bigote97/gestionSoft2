
class empleadoEventual:
    def __init__(self, nombre, apellido, dni, salario, ventas):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.ventas = ventas

    def calcularIngresoTotal(self):
        total = self.salario + self.calcularComision()
        return total
    
    def calcularComision(self):
        aux = 0
        for i in self.ventas:
            aux = aux + i
        comision = aux * 0.5
        return comision
    def mostrarEmpleado(self):
        print('Nombre: ', self.nombre)
        print('Apellido: ', self.apellido)
        print('Dni: ', self.dni)
        print('Salario: $', self.salario)
        print('Ventas: ', self.ventas)

pedrito = empleadoEventual('pedro', 'ferreyra', 40317631, 20000, [20, 30, 40])
pedrito.mostrarEmpleado()
total = pedrito.calcularIngresoTotal()
print(total)
#pedrito.calcularIngresoTotal