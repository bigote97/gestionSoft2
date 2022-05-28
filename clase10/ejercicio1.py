#! /usr/bin/python3
#Para que pueda manejar fechas:
import datetime
from pickle import TRUE

#Guardamos en una variable la próxima id disponible:
ultima_id = 0

class Nota:
    '''Representa una nota en el anotador. Tiene texto, etiquetas (separadas 
    por espacios) y se puede buscar por texto'''
    def __init__(self, texto, etiquetas=''):
        '''Inicializa la nota con un texto, y opcionalmente, con etiquetas 
        separadas por espacios. Automáticamente define fecha de creación e id'''
        self.texto = texto
        self.etiquetas = etiquetas

        #Fecha de hoy
        self.fecha_creacion = datetime.date.today()

        # Le sumamos 1 a la ultima_id guardada...
        global ultima_id
        ultima_id += 1

        # ... y asignamos ese número como id de esta Nota:
        self.id = ultima_id
    def mostrar(self):
        print('Nota: ', self.texto)
        print('Etiqueta: ', self.etiquetas)
        print('ID: ', self.id)
        print('Creada: ', self.fecha_creacion)

    def coincide(self, filtro):
        '''Determina si la nota coincide con el filtro de búsqueda. Retorna 
        True si es así y False de lo contrario
        
        Busca tanto en el texto como en las etiquetas y distingue mayúsculas de
        minúsculas '''
        if ((filtro in self.texto) or (filtro in self.etiquetas)):
            return True
        else:
            return False
        #TODO: Construir este método
        # Recordatorio para buscar en una cadena:
        # if {subcadena} in {cadena}:
        # Ej:
        # if 'ten' in 'entretenido':  ---> sale por True
        # if 'blabla' in 'entretenido': ---> sale por False

almacen_notas = [
Nota('El texto de la nota', 'prueba'),
Nota('El texto de la nota al cuadradp', 'prueba'),
Nota('El texto de la nota al cubo', 'prueba'),
Nota('El texto de la nota al la cuarta', 'prueba'),
Nota('El texto de la nota al la quinta', 'prueba')
]

def menu():
    print('''Ingrese:
        1-para cargar una nueva nota
        2-para buscar en una nota
        0 (o cualquier otro digito)-para salir
        ''')

def crear_nota(texto, etiqueta):
    almacen_notas.append(Nota(texto, etiqueta))

def buscar_en_notas():
    buscar = input('Ingrese palabra a buscar: ')

    for i in almacen_notas:
        if (i.coincide(buscar)):
            print(buscar, ' es la nota numero: ', i.id)
            i.mostrar()
menu()
run = int(input())
while( run == 1 or run == 2):
    if run == 1:
        crear_nota(input('Ingrese la nota: '), input('Ingrese la etiqueta de la nota: '))
    else:
        buscar_en_notas()
    menu()
    run = int(input())