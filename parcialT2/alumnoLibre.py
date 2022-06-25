#!/usr/bin/python3

class AlumnoLibre:
    def __init__(self,nombre, apellido, dni, nota_examen_final):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.nota_examen_final = nota_examen_final

    def obtener_nota_final(self):
        return self.nota_examen_final
        
    def mostrar_datos(self):
        texto = f"Estudiante: {self.nombre} {self.apellido}\n"
        texto+= f"DNI: {self.dni}\n"
        texto+= "Nota: " + str(self.obtener_nota_final()) + "\n"
        return texto

