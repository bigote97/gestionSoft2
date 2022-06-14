from random import randint
from permanentes import empleadoPermanente
from eventuales import empleadoEventual
import names

class personal:
    def __init__(self):
        empleados = []
        empleados.append({
            'nombre': 'augusto',
            'apellido': 'rossetti',
            'dni': 40317631,
            'salario': 1200,
            'antiguedad': 2
        })
        for i in range(10):
            temp = {
                'nombre': names.get_first_name(),
                'apellido': names.get_last_name(),
                'dni': randint(10000000, 99999999),
                'salario': randint(10000, 99999),
            }
            aux = randint(0, 1)
            if (aux == 1):
                auxVentas = randint(1, 9)
                temp['ventas'] = []
                for i in range(auxVentas):
                    temp['ventas'].append(randint(1000, 9999))
                # empleadoEventual(temp['nombre'], temp['apellido'], temp['dni'], temp['salario'], temp['ventas'])
            else:
                temp['antiguedad'] = randint(0, 9)
                # empleadoPermanente(temp['nombre'], temp['apellido'], temp['dni'], temp['salario'], temp['antiguedad'])
            
            empleados.append(temp)
        self.empleados = empleados.copy()

    def verificaDni(self, dni):
        retorna = None
        for empleado in self.empleados:
            print(empleado)
            if empleado.dni() == dni:
                if ('ventas' in empleado):
                    retorna = empleadoEventual(empleado['nombre'], empleado['apellido'], empleado['dni'], empleado['salario'], empleado['ventas']) 
                else:   
                    retorna = empleadoPermanente(empleado['nombre'], empleado['apellido'], empleado['dni'], empleado['salario'], empleado['antiguedad'])
                    
        return retorna
    
    def listarEmpleados(self):
        for empleado in self.empleados:
            if hasattr(empleado, 'mostrarEmpleado'):
                retorna = empleado
            else:
                if ('ventas' in empleado):
                    retorna = empleadoEventual(empleado['nombre'], empleado['apellido'], empleado['dni'], empleado['salario'], empleado['ventas']) 
                else:   
                    retorna = empleadoPermanente(empleado['nombre'], empleado['apellido'], empleado['dni'], empleado['salario'], empleado['antiguedad'])
               
            print(retorna.mostrarEmpleado())
    
    def agregarEmpleado(self, nombre, apellido, dni, salario, extra):
        if (self.verificaDni(dni) == None):
            if (type(extra) is list):
                temp = empleadoEventual(nombre, apellido, dni, salario, extra)            
                self.empleados.append(temp)
                retorna = temp
            else:   
                temp = empleadoPermanente(nombre, apellido, dni, salario, extra)
                self.empleados.append(temp)
                retorna = temp
        else:
            retorna = 'Usuario existente'
        return retorna

    def verificaString(self, str):
        aux = None
        for empleado in self.empleados:
            if (str in empleado['nombre'] or str in empleado['apellido']):
                aux = []
                if ('ventas' in empleado):
                    retorna = empleadoEventual(empleado['nombre'], empleado['apellido'], empleado['dni'], empleado['salario'], empleado['ventas']) 
                else:   
                    retorna = empleadoPermanente(empleado['nombre'], empleado['apellido'], empleado['dni'], empleado['salario'], empleado['antiguedad'])
                aux.append(retorna)
        return aux