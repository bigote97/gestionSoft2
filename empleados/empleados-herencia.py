#!/usr/bin/python3

from empleadoPermanente import EmpleadoPermanente
from empleadoEventual import EmpleadoEventual

class Personal:
    def __init__(self):
        self.lista_empleados = []

    def agregar_empleado(self, nombre, apellido, dni, salario, antiguedad = None, ventas = None):
        if antiguedad:
            e = EmpleadoPermanente(nombre, apellido, dni, salario, antiguedad)
        elif ventas:
            e = EmpleadoEventual(nombre, apellido, dni, salario, ventas)
        else:
            return None

        self.lista_empleados.append(e)

    def buscar_por_dni(self, dni_para_buscar):
        '''Un método que reciba un nro de DNI y retorne el empleado que tiene
        ese DNI, o None si no hay ninguno.'''
        for un_empleado in self.lista_empleados:
            if un_empleado.dni == dni_para_buscar:
                return un_empleado
        return None

    def buscar_por_nombre_apellido(self, texto_a_buscar):
        '''Un método que reciba un texto, y retorne una lista de empleados cuyo
        nombre y/o apellido coincida (total o parcialmente) con ese texto.'''
        empleados_coincidentes = []
        for un_empleado in self.lista_empleados:
            if un_empleado.coincide(texto_a_buscar):
                empleados_coincidentes.append(un_empleado)
        return empleados_coincidentes