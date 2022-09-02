from empleado import Empleado

class EmpleadoEventual(Empleado):
  def __init__(self, nombre, apellido, dni, salario, ventas):
    super().__init__(nombre, apellido, dni, salario)
    self.ventas = ventas

  def calcular_comision(self):
    total_ventas = 0
    for una_venta in self.ventas:
      total_ventas = total_ventas + una_venta

    # O bien:
    # total_ventas = sum(self.ventas)
    
    porcentaje_comision = 0.05
    comision = total_ventas * porcentaje_comision
    return comision

  def calcular_ingreso_total(self):
    ingreso_total = super().calcular_ingreso_total()
    return ingreso_total

  def coincide(self, texto_a_buscar):
    coincide = super().coincide(texto_a_buscar)
    return coincide

  def mostrar_datos(self):
    texto = super().mostrar_datos()
    texto += f"Ventas: {self.ventas}\n"
    return texto