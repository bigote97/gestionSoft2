#!/usr/bin/python3

# Implementar aquí la clase AlumnoPresencial

class AlumnoPresencial:
    def __init__(self, nombre, apellido, dni, notas_tp, asist):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.notas_tp = notas_tp
        self.asist = asist

    def obtener_nota_final(self):
        tp_no_aprobado = False
        for nota in self.notas_tp:
            if nota < 4:
                tp_no_aprobado = True
                break 
        if( (self.asist < 75) or tp_no_aprobado):
            return 1
        else:
            todo_aprobado = False
            cantidad_tp = 0
            suma_notas = 0
            for nota in self.notas_tp:
                if nota < 6:
                    todo_aprobado = False
                else: 
                    todo_aprobado = True

                cantidad_tp += 1
                suma_notas += nota
            if todo_aprobado:
                promedio = suma_notas/cantidad_tp
                return promedio
            else:
                promedio = (suma_notas/cantidad_tp) - 1
                return promedio
        
    def mostrar_datos(self):
        texto = f"Estudiante: {self.nombre} {self.apellido}\n"
        texto+= f"DNI: {self.dni}\n"
        texto+= "Nota: " + str(self.obtener_nota_final()) + "\n"
        return texto