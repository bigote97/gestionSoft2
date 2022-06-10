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
    
    def nuevoEmpleado(self, nombre, apellido, dni, salario, ventas):
        self.verificaDni(dni)
    
    def verificaDni(dni):
        for empleado in range(empleados):
            if empleado.dni == dni:
                return True
                break