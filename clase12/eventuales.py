class empleadoEventual:
    def __init__(self, nombre, apellido, dni, salario, ventas):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.ventas = ventas

    def calcularSalario(self):
        aux
        for i in range(self.ventas):
            aux = aux + self.ventas[i]
        comision = aux * 0.5
        total = self.salario + comision
        return total
    
    def nuevoEmpleado(self):
        if not self.verificaDni(self.dni):
            temp = {
                'nombre': self.nombre,
                'apellido': self.apellido,
                'dni': self.dni,
                'salario': self.salario,
                'ventas': self.ventas
            }
            empleados.append(temp)

    def listarEmpleados(self):
        temp = []
        for empleado in range(empleados):
            if (dict.has_key('ventas')):
                temp.append(empleado)
        return temp

    def verificaDni(dni):
        for empleado in range(empleados):
            if empleado.dni == dni:
                return True
                break
        return False