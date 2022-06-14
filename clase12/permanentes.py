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
        string = f'''
        Nombre:  {self.nombre}
        Apellido:  {self.apellido}
        Dni:  {self.dni}
        Salario: $ {self.salario}
        Antiguedad:  {self.antiguedad}'''
        return string