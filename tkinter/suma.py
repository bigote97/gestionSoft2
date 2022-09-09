#!/usr/bin/python3

class Suma:
	def __init__(self, n1, n2, n3:None, n4:None, n5:None):
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3
		self.n4 = n4
		self.n5 = n5

	def mostrar_resultado(self):
		suma = self.n1 + self.n2
		if (self.n3 != None):
			suma += self.n3
		return suma

	def mostrar_operacion_completa(self):
		suma = str(self.n1) + ' + ' + str(self.n2) 
		if (self.n3 != None):
			suma += ' + ' + str(self.n3) 
		return suma + ' = ' \
			+ str(self.mostrar_resultado())


