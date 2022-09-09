#!/usr/bin/python3
from suma import Suma

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

s = Suma(n1, n2)

print(s.mostrar_operacion_completa())


