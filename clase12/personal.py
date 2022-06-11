from random import randint
import permanentes from empleadoPermanente
import eventuales from empleadoEventual
import names

class personal:
    def __init__(self):
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

    def nuevoEmpleado(self, nombre, apellido, dni, salario, extra):
