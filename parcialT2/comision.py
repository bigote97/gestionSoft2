#!/usr/bin/python3

from alumnoLibre import AlumnoLibre
from alumnoPresencial import AlumnoPresencial

class Comision:
    def __init__(self):
        self.lista_de_alumnos = []
        # Para pruebas: se cargan algunos alumnos:
        self.cargar_alumnos_para_pruebas()

    def cargar_alumnos_para_pruebas(self):
        a1 = AlumnoLibre("Carlos", "Gardel", "12345678", 9)
        self.lista_de_alumnos.append(a1)

        a2 = AlumnoLibre("Mercedes", "Sosa", "12345679", 8)
        self.lista_de_alumnos.append(a2)

        a3 = AlumnoPresencial("Julio", "Sosa", "11111111", [6,7,8,9], 90)
        self.lista_de_alumnos.append(a3)

        a4 = AlumnoPresencial("Alfredo", "Zitarrosa", "22222222", [6,3,8,9], 80)
        self.lista_de_alumnos.append(a4)

        a5 = AlumnoPresencial("Ramona", "Galarza", "33333333", [6,10,8,9], 50)
        self.lista_de_alumnos.append(a5)

    def agregar_alumno_libre(self, nombre, apellido, dni, nota_examen_final):
        a = AlumnoLibre(nombre, apellido, dni, nota_examen_final)
        self.lista_de_alumnos.append(a)

    def agregar_alumno_presencial(self, nombre, apellido, dni, notas_tp, asist):
        a = AlumnoPresencial(nombre, apellido, dni, notas_tp, asist)
        self.lista_de_alumnos.append(a)

    def buscar_por_dni(self, dni_a_buscar):
        for alumno in self.lista_de_alumnos:
            if alumno.dni == dni_a_buscar:
                return alumno
        return None

    def obtener_mejor_nota(self):
        '''Retorna el objeto Alumno cuya nota final sea la mayor de la lista
        self.lista_de_alumnos. (Por simplicidar, suponer que **no** habrá dos
        estudiantes que "compartan" el primer puesto)'''
        mejor_nota = 0
        for alumno in self.lista_de_alumnos:
            nota_alumno = alumno.obtener_nota_final()
            if nota_alumno > mejor_nota:
                mejor_nota = nota_alumno
                alumno_con_mejor_nota = alumno

        return alumno_con_mejor_nota

