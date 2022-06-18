class EmpleadoEventual:
  def __init__(self, nombre, apellido, dni, salario, ventas):
    self.nombre = nombre
    self.apellido = apellido
    self.dni = dni
    self.salario = salario
    self.ventas = ventas

  def calcular_comision(self):
    porcentaje_comision = 0.05
    total_ventas = 0
    for venta in self.ventas:
      total_ventas = total_ventas + venta
    comision = total_ventas * porcentaje_comision
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
      Ventas:  {self.ventas}'''
    return string