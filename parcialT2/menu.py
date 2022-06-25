#!/usr/bin/python3

from comision import Comision
import sys

class Menu:
    def __init__(self):
        self.comision = Comision()

    def ejecutar(self):
        while True:
            self.elegir_opcion()

    def elegir_opcion(self):
        print ('''
1- Agregar alumno libre
2- Agregar alumno presencial
3- Buscar alumno por DNI
4- Obtener el mejor promedio
5- Salir''')
        opcion = int(input("Elija la opción: "))

        if opcion == 1:
            self.agregar_libre()
        elif opcion == 2:
            self.agregar_presencial()
        elif opcion == 3:
            self.buscar_por_dni()
        elif opcion == 4:
            self.mejor_promedio()
        elif opcion == 5:
            self.salir()


    def agregar_libre(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        dni = input("Ingrese el dni: ")
        nota_final = int(input("Ingrese la nota_final: "))
        self.comision.agregar_alumno_libre(nombre, apellido, dni, nota_final)

    def agregar_presencial(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        dni = input("Ingrese el dni: ")
        while True:
            asist = int(input("Porcentaje de asistencia"))
            if asist < 0 or asist > 100:
                print("Error en el porcentaje de asistencia")
            else:
                break
        cantidad_de_notas = int(input("Ingrese cuántos TP hubo: "))

        notas = []
        for i in range(cantidad_de_notas):
            while True:
                nota = int(input("Ingrese la siguiente nota: "))
                if nota > 0 and nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Error: la nota debe estar entre 1 y 10")

        self.comision.agregar_alumno_presencial(nombre, apellido, dni, notas, asist)


    def buscar_por_dni(self):
        dni_a_buscar = input("Ingrese DNI para buscar: ")
        alumno = self.comision.buscar_por_dni(dni_a_buscar)
        if alumno:
            print(alumno.mostrar_datos())
        else:
            print("No se encontraron estudiantes con ese DNI")

    def mejor_promedio(self):
        alumno = self.comision.obtener_mejor_nota()
        if alumno:
            print('El alumno con mejor promedio es:')
            print(alumno.mostrar_datos())
        else:
            print("No hay ningún alumno en la comisión")
        
    def salir(self):
        print("Gracias por utilizar el sistema.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().ejecutar()
