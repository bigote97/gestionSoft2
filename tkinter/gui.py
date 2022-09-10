#!/usr/bin/python3

import tkinter
from tkinter import ttk, font
from suma import Suma

class Aplicacion:
	def __init__(self):
		self.raiz = tkinter.Tk()
		self.raiz.title("Sumar")
		self.raiz.geometry('450x450')

		fuente = font.Font(weight='bold')

		self.etiq1 = ttk.Label(self.raiz, text="Primer número: ", font=fuente)
		self.etiq2 = ttk.Label(self.raiz, text="Segundo número: ", font=fuente)
		self.etiq3 = ttk.Label(self.raiz, text="tercero número: ", font=fuente)
		self.etiq4 = ttk.Label(self.raiz, text="Cuarto número: ", font=fuente)
		self.etiq5 = ttk.Label(self.raiz, text="Quinto número: ", font=fuente)

		self.ctext1 = ttk.Entry(self.raiz, width=30)
		self.ctext2 = ttk.Entry(self.raiz, width=30)
		self.ctext3 = ttk.Entry(self.raiz, width=30)
		self.ctext4 = ttk.Entry(self.raiz, width=30)
		self.ctext5 = ttk.Entry(self.raiz, width=30)
		self.separador = ttk.Separator(self.raiz, orient=tkinter.HORIZONTAL)

		self.boton1 = ttk.Button(self.raiz, text="Sumar",
						command=self.sumar)
		self.boton2 = ttk.Button(self.raiz, text="Salir", command=quit)

		self.texto_resultado = tkinter.StringVar()
		self.texto_resultado.set('... ...')
		self.resultado = ttk.Label(self.raiz, textvariable=self.texto_resultado,
						font=fuente)

		self.etiq1.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
		self.ctext1.pack(side=tkinter.TOP, fill=tkinter.X, expand=True, padx=5, pady=5)
		
		self.etiq2.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
		self.ctext2.pack(side=tkinter.TOP, fill=tkinter.X, expand=True, padx=5, pady=5)

		self.etiq3.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
		self.ctext3.pack(side=tkinter.TOP, fill=tkinter.X, expand=True, padx=5, pady=5)
		
		self.etiq4.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
		self.ctext4.pack(side=tkinter.TOP, fill=tkinter.X, expand=True, padx=5, pady=5)
	
		self.etiq5.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
		self.ctext5.pack(side=tkinter.TOP, fill=tkinter.X, expand=True, padx=5, pady=5)

		self.separador.pack(side=tkinter.TOP, fill=tkinter.X, expand=True, padx=5, pady=5)

		self.resultado.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True, padx=5, pady=5)

		self.boton1.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
		self.boton2.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)

		self.ctext1.focus_set()

		self.raiz.bind('<Return>', self.sumar)

		self.raiz.mainloop()

	def sumar(self, event=None):
		inputs =[]
		inputs.append(self.ctext1.get())
		inputs.append(self.ctext2.get())
		inputs.append(self.ctext3.get())
		inputs.append(self.ctext4.get())
		inputs.append(self.ctext5.get())

		for input in range(len(inputs)):
			if (inputs[input] == ''):
				inputs[input] = None
			else:
				inputs[input] = int(inputs[input])
		
		s = Suma(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4])

		texto = s.mostrar_suma_completa()
		
		self.texto_resultado.set(texto)
		print(texto)



def main():
	mi_programa = Aplicacion()
	return 0

if __name__ == "__main__":
	main()

# https://docs.hektorprofe.net/python/interfaces-graficas-con-tkinter/
# https://python-para-impacientes.blogspot.com/p/tutorial-de-tkinter.html
