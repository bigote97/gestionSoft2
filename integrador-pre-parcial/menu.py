from personal import Personal

import os

class Menu:
  def __init__(self):
    self.personal = Personal()

  def mostrar_menu(self):
    print('''
      1_ Agregar nuevo empleado
      2_ Buscar DNI
      3_ Buscar por nombre o apellido
      4_ Ver comision dado un DNI
      5_ Listar empleados
      6_ Salir del programa
    ''')
  
  def clearConsole(self):
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
      command = 'cls'
    os.system(command)

  def ejecutar(self):
    while True:
      self.mostrar_menu()
      opcion = input('Ingrese opcion elegida: ')
      if (opcion == '1'):
        self.menu_agregar_empleado()
      if (opcion == '2'):
        self.menu_buscar_dni()
      if (opcion == '3'):
        self.menu_buscar_str()
      if (opcion == '4'):
        self.menu_dado_dni()
      if (opcion == '5'):
        self.menu_listar_empleados()
      if (opcion == '6'):
        break
    self.clearConsole()
    print('Programa finalizado')

  def menu_agregar_empleado(self):
    self.clearConsole()
    dni_ne = int(input('Ingrese el DNI del empleado '))
    existe = self.personal.buscar_dni(dni_ne)
    if (type(existe) is None):
      print('Empleado ya registrado')
      print(existe)
    else:
      nombre_ne = input('Ingrese nombre del empleado ')
      apellido_ne = input('Ingrese apellido del empleado ')
      salario_ne = int(input('Ingrese salario del empleado '))
      tipo_ne = input('Ingrese E para empleado eventual o P para permanente ')
      ventas_ne = []
      if (tipo_ne == 'E' or tipo_ne == 'e'):
        venta = int(input('Ingrese monto de venta '))
        while True:
          ventas_ne.append(venta)
          if venta != 0:
            venta = int(input('Ingrese monto de venta o 0 para finalizar '))
          else:
            break
        nuevo_empleado = self.personal.agregar_empleado(nombre_ne, apellido_ne, dni_ne, salario_ne, ventas_ne)
      elif(tipo_ne == 'P' or tipo_ne == 'p'):
        antiguedad_ne = int(input('Ingrese antiguedad del empleado '))
        nuevo_empleado = self.personal.agregar_empleado(nombre_ne, apellido_ne, dni_ne, salario_ne, antiguedad_ne)
      print('Empleado registrado con exito')
      print(nuevo_empleado.mostrar_empleado())

  def menu_buscar_dni(self):
    self.clearConsole()
    dni_a_buscar = int(input('Ingrese DNI a buscar '))
    resultado = self.personal.buscar_dni(dni_a_buscar)
    if (resultado is None):
      print('DNI no encontrado')
    else:
      print(resultado.mostrar_empleado())
  
  def menu_buscar_str(self):
    self.clearConsole()
    str_a_buscar = input('Ingrese nombre o apellido a buscar ')
    resultado = self.personal.buscar_string(str_a_buscar)
    if (len(resultado) == 0):
      print('nombre o apellido no encontrados')
    else:
      for empleado in resultado:
        print(empleado.mostrar_empleado())
 
  def menu_dado_dni(self):
    self.clearConsole()
    dni_a_buscar = int(input('Ingrese DNI a buscar '))
    resultado = self.personal.buscar_dni(dni_a_buscar)
    if (resultado is None):
      print('DNI no encontrado')
    else:
      print('EL salario total es: ')
      print(resultado.calcular_salario_total())
      print('La comision es: ')
      print(resultado.calcular_comision())
  
  def menu_listar_empleados(self):
    self.clearConsole()
    if(len(self.personal.lista_empleados) != 0):
      for empleado in self.personal.lista_empleados:
        print(empleado.mostrar_empleado())
    else:
      print('No hay empleados en la lista')

menu = Menu()
menu.ejecutar()