empleados = [
    '40317631':{
        nombre: 'augusto',
        apellido: 'Rossetti',
        
    }
]



class empleadoEvantual:
    def __init__(self, nombre, apellido, dni, salario, ventas):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.ventas = ventas

    def calcularSalario(self):
        comision = totalVentas * 0.5
        total = self.salario + comision
        return total




class empleadoPermanente:
    def __init__(self, nombre, apellido, dni, salario, antiguedad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.antiguedad = antiguedad
    def calcularSalario(self):
        comision = (self.salario*self.antiguedad)/100
        total = self.salario + comision