from empleadoPermanente import EmpleadoPermanente
from empleadoEventual import EmpleadoEventual

class Personal:
  def __init__(self):
    lista_empleados = []
    self.lista_empleados = lista_empleados
  
  def agregar_empleado(self, nombre, apellido, dni, salario, antiguedad = None, ventas = None):
    if (antiguedad):
      nuevo_empleado = EmpleadoPermanente(nombre, apellido, dni, salario, antiguedad)
    elif (ventas):
      nuevo_empleado = EmpleadoEventual(nombre, apellido, dni, salario, ventas)
    else:
      return None
    self.lista_empleados.append(nuevo_empleado)
    return nuevo_empleado

  def buscar_dni(self, dni_a_buscar):
    for empleado in self.lista_empleados:
      if (empleado.dni == dni_a_buscar):
        return empleado
    return None

  def buscar_string(self, str_a_buscar):
    lista_encontrados = []
    for empleado in self.lista_empleados:
      if ((str_a_buscar.lower() in empleado.nombre.lower()) or (str_a_buscar.lower() in empleado.apellido.lower())):
        lista_encontrados.append(empleado)
    return lista_encontrados