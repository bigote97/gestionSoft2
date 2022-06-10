from random import randint
import names


empleados = []

for i in range(10):
    temp = {
        'nombre': names.get_first_name(),
        'apellido': names.get_last_name(),
        'dni': randint(10000000, 99999999),
        'salario': randint(10000, 99999),
    }
    aux = randint(0, 1)
    if (aux == 1):
        temp['ventas']= randint(1000, 9999)
    else:
        temp['antiguedad']= randint(0, 9)
    empleados.append(temp)
for j in range(10):
    print(empleados[j])


class empleadoEvantual:
    def __init__(self, nombre, apellido, dni, salario, ventas):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.ventas = ventas

    def calcularSalario(self):
        comision = ventas * 0.5
        total = self.salario + comision
        return total




class empleadoPermanente:
    def __init__(self, nombre, apellido, dni, salario, antiguedad):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.salario = salario
        self.antiguedad = antiguedad
    def calcularSalario(self):
        comision = (self.salario*self.antiguedad)/100
        total = self.salario + comision