#!/usr/bin/python3

from personal import Personal
from empleadoPermanente import EmpleadoPermanente
from empleadoEventual import EmpleadoEventual
import sys

class Menu:
    def __init__(self):
        self.personal = Personal()

    def ejecutar(self):
        while True:
            self.elegir_opcion()

    def elegir_opcion(self):
        print ('''
1- Agregar un empleado, tanto eventual como permanente.
2- Buscar un empleado por DNI.
3- Buscar un empleado por nombre y/o apellido.
4- Calcular comisión e ingreso total de un empleado.
5- Mostrar un listado de todos los empleados.
6- Salir del programa.''')
        opcion = int(input("Elija la opción: "))

        if opcion == 1:
            self.agregar_empleado()
        elif opcion == 2:
            self.buscar_por_dni()
        elif opcion == 3:
            self.buscar_por_nombre_apellido()
        elif opcion == 4:
            self.calcular_comision()
        elif opcion == 5:
            self.lista_completa()
        elif opcion == 6:
            self.salir()

    def agregar_empleado(self):
        while True:
            tipo = input("Ingrese tipo de empleado (Eventual o Permanente) [E/P]")
            if tipo in [ 'e', 'E', 'p', 'P']:
                break
            else:
                print("Error: ingrese 'e' o 'p'")
        nombre = input("Ingrese el nombre del Empleado: ")
        apellido = input("Ingrese el apellido del Empleado: ")
        dni = input("Ingrese el dni del Empleado: ")
        salario = int(input("Ingrese el salario del Empleado: "))

        if tipo == 'p' or tipo == 'P':
            antiguedad = int(input("Ingrese la antigüedad: "))
            ventas = None
        elif tipo == 'e' or tipo == 'E':
            antiguedad = None
            ventas = []
            while True:
                una_venta = int(input("Ingrese el monto de una venta, 0 para finalizar"))
                if una_venta == 0:
                    break
                ventas.append(una_venta)

        self.personal.agregar_empleado(nombre, apellido, dni, salario, antiguedad, ventas)

    def buscar_por_dni(self):
        dni_a_buscar = input("Ingrese el DNI a buscar")
        empleado = self.personal.buscar_por_dni(dni_a_buscar)
        if empleado:
            # Mostramos los datos del empleado:
            print(empleado.mostrar_datos())
        else:
            print("No se encontró un empleado con ese DNI")

    def buscar_por_nombre_apellido(self):
        texto_a_buscar = input("Ingrese parte del nombre o apellido a buscar")
        empleados = self.personal.buscar_por_nombre_apellido(texto_a_buscar)
        if empleados:
            # Mostramos los datos del empleado:
            for e in empleados:
                print(e.mostrar_datos())
        else:
            print("No se encontró ningún empleado con ese nombre o apellido")

    def calcular_comision(self):
        dni_a_buscar = input("Ingrese el DNI a buscar")
        empleado = self.personal.buscar_por_dni(dni_a_buscar)
        if empleado:
            print(empleado.mostrar_datos())
            print("Comision: " + str(empleado.calcular_comision()))
            print("Ingreso total: " + str(empleado.calcular_ingreso_total()))
        else:
            print("No se encontró un empleado con ese DNI")

    def lista_completa(self):
        for empleado in self.personal.lista_empleados:
            print(empleado.mostrar_datos())
            print("Comision: " + str(empleado.calcular_comision()))
            print("Ingreso total: " + str(empleado.calcular_ingreso_total()))
            print("=====================================")

    def salir(self):
        '''Muestra un mensaje y sale del sistema'''
        print("Gracias por utilizar el sistema.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().ejecutar()

