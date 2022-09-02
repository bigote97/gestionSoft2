from empleadoPermanente import EmpleadoPermanente
from empleadoEventual import EmpleadoEventual

class Empleado:
  def __init__(self, nombre, apellido, dni, salario):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.salario = salario

  def calcular_ingreso_total(self):
    ingreso_total = self.salario + self.calcular_comision()
    return ingreso_total

  def coincide(self, texto_a_buscar):
    if (texto_a_buscar in self.nombre or texto_a_buscar in self.apellido):
      return True
    else:
      return False

  def mostrar_datos(self):
    texto = f"Nombre y apellido: {self.nombre} {self.apellido}\n"
    texto += f"DNI: {self.dni} - Salario: {self.salario}\n"
    return texto