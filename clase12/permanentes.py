class empleadoPermanente:
    def __init__(self, nombre, apellido, dni, salario, antiguedad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.antiguedad = antiguedad

    def calcularIngresoTotal(self):
        total = self.salario + self.calcularComision()
        return total
    
    def calcularComision(self):
        comision = (self.salario*self.antiguedad)/100
        return comision
    def mostrarEmpleado(self):
        print('Nombre: ', self.nombre)
        print('Apellido: ', self.apellido)
        print('Dni: ', self.dni)
        print('Salario: $', self.salario)
        print('Antiguedad: ', self.antiguedad)

pedrito = empleadoPermanente('pedro', 'ferreyra', 40317631, 20000, 20)
pedrito.mostrarEmpleado()
total = pedrito.calcularIngresoTotal()
print(total)