class EmpleadoPermanente:
  def __init__(self, nombre, apellido, dni, salario, antiguedad):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.salario = salario
    self.antiguedad = antiguedad

  def calcular_comision(self):
    comision = self.salario * self.antiguedad / 100
    return comision
  
  def calcular_salario_total(self):
    salario_total = self.salario + self.calcular_comision()
    return salario_total
  
  def mostrar_empleado(self):
    string = f'''
      Nombre:  {self.nombre}
      Apellido:  {self.apellido}
      Dni:  {self.dni}
      Salario: $ {self.salario}
      Antiguedad:  {self.antiguedad}'''
    return string