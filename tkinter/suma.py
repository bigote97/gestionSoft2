#!/usr/bin/python3

class Suma:
	def __init__(self, n1, n2, n3, n4, n5):
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3
		self.n4 = n4
		self.n5 = n5

	def mostrar_suma(self):
		suma = self.n1 + self.n2
		if (self.n3):
			suma += self.n3
		if (self.n4 != None):
			suma += self.n4
		if (self.n5 != None):
			suma += self.n5
		return suma

	def mostrar_suma_completa(self):
		suma = str(self.n1) + ' + ' + str(self.n2) 
		if (self.n3 != None):
			suma += ' + ' + str(self.n3) 
		if (self.n4 != None):
			suma += ' + ' + str(self.n4) 
		if (self.n5 != None):
			suma += ' + ' + str(self.n5) 
		return suma + ' = ' \
			+ str(self.mostrar_suma())


