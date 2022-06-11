from random import randint
from permanentes import empleadoPermanente
from eventuales import empleadoEventual
import names

class personal:
    def __init__(self, nombre, apellido, dni, salario, extra):
        empleados = []
        for i in range(10):
            temp = {
                'nombre': names.get_first_name(),
                'apellido': names.get_last_name(),
                'dni': randint(10000000, 99999999),
                'salario': randint(10000, 99999),
            }
            aux = randint(0, 1)
            if (aux == 1):
                auxVentas = randint(1, 99)
                temp['ventas'] = []
                for i in range(auxVentas):
                    temp['ventas'].append(randint(1000, 9999))
                    
            else:
                temp['antiguedad'] = randint(0, 9)
            
            empleados.append(temp)
        self.empleados = empleados
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.ventas = extra

    def verificaDni(self, dni):
        for empleado in range(self.empleados):
            if empleado.dni == dni:
                return True
                break
        return False
    
    def listarEmpleados(self):
        for empleado in range(self.empleados):
            print(empleado)
    def nuevoEmpleado(self):
        if not self.verificaDni(self.dni):
            temp = {
                'nombre': self.nombre,
                'apellido': self.apellido,
                'dni': self.dni,
                'salario': self.salario
            }
            if type(self.extra) is list:
                temp['ventas'] = []
                temp['ventas'] = self.extra
            else:
                temp['antiguedad'] = self.extra
            self.empleados.append(temp)
            retorna = temp
        else:
            retorna = 'Usuario existente'
        return retorna

pedro = personal('pedro', 'ferreyra', 40317631, 20000, 20)

pedro.nuevoEmpleado()
