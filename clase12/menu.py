from permanentes import empleadoPermanente
from eventuales import empleadoEventual
from personal import personal
import os
import time

class menu:
	def __init__ (self):
		self.personal = personal()

	def ejecutar(self):
		while True:
			rta = input('''
			1_ Agregar nuevo empleado
			2_ Buscar Dni
			3_ Buscar por nombre o apellido
			4_ Dado Dni ver comision y sueldo
			5_ Listar todos los empleados
			6_ Salir
			''')
			if (rta == '1'):
				self.agregarEmpleado()
			elif (rta == '2'):
				self.buscarDni()
			elif (rta == '3'):
				self.buscarStr()
			elif (rta == '4'):
				self.verMontosDni()
			elif (rta == '5'):
				self.listarEmpleados()
			elif (rta == '6'):
				for i in range(5, 1, 1):
					print('Cerrando programa', i)
					time.sleep(2.5)
					os.system('cls')
				break
  
	def agregarEmpleado(self):
		print('Cargar nuevo empleado:')
		dni = int(input('Ingrese DNI: '))
		if (self.personal.verificaDni(dni) == None):
			nombre = input('Ingrese nombre: ')
			apellido = input('Ingrese apellido: ')
			salario = input('Ingrese salario: ')
			rta = input('Es un empleado eventual? Y = Si, N = No ')
			if (rta == 'y' or rta == 'Y'):
				extra = []
				sigue = True
				while sigue:
					aux = int(input('Ingrese ventas: '))
					extra.append(aux)
					rta = input('Ingresara una nueva venta? Y = Si, N = No ')
					if (rta == 'y' or rta == 'Y'):
						sigue = True
					else:
						sigue = False
			else:
				extra = int(input('Ingrese antiguedad: '))
			empleado = self.personal.agregarEmpleado(nombre, apellido, dni, salario, extra)
			print(empleado.mostrarEmpleado())
		else:
			print('''
	Empleado existente
			''')

	def buscarDni(self):
		dni = int(input('Ingrese DNI a buscar: '))
		empleado = self.personal.verificaDni(dni)
		if (empleado == None):
			print('No se encontro un empleado con ese DNI')
		else:
			print(empleado.mostrarEmpleado())
	
	def buscarStr(self):
		str = input('Ingrese nombre o apellido a buscar: ')
		resultados = self.personal.verificaString(str)
		if (resultados == None):
			print('No hay usuarios con esas especificaciones')
		else:
			for resultado in resultados:
				print(resultado.mostrarEmpleado())

	def verMontosDni(self):
		dni = int(input('Ingrese DNI a buscar: '))
		empleado = self.personal.verificaDni(dni)
		if (empleado == None):
			print('No se encontro un empleado con ese DNI')
		else:
			print(empleado.mostrarEmpleado())
			print('Comision: ', empleado.calcularComision())
			print('Salario total: ', empleado.calcularIngresoTotal())
	
	def listarEmpleados(self):
		self.personal.listarEmpleados()



menu = menu()
menu.ejecutar()
