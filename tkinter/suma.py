#!/usr/bin/python3

class Suma:
	def __init__(self, n1, n2, n3:None, n4:None, n5:None):
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3
		self.n4 = n4
		self.n5 = n5

	def mostrar_resultado(self):
		return self.n1 + self.n2 + self.n3 + self.n4 + self.n5

	def mostrar_operacion_completa(self):
		return str(self.n1) + ' + ' + str(self.n2) + ' = ' \
			+ str(self.mostrar_resultado())


