
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
        procentaje_comision = 0.5
        for i in self.ventas:
            aux = aux + i
        comision = aux * procentaje_comision
        return comision
    
    def mostrarEmpleado(self):
        string = f'''
        Nombre:  {self.nombre}
        Apellido:  {self.apellido}
        Dni:  {self.dni}
        Salario: $ {self.salario}
        Ventas:  {self.ventas}'''
        return string
        
    def numeroDni(self):
        return self.dni

    def esPermante():
        return False