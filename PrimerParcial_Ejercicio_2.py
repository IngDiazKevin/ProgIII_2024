import os

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def __str__(self):
        return f'Nombre: {self.nombre} - Edad: {self.edad} - Carrera: {self.carrera}'

class RegistroEstudiantes:
    def __init__(self):
        self.nombre_archivo = 'estudiantes.txt'

    def agregar_estudiante(self, estudiante):
         with open(self.nombre_archivo, 'a') as archivo:
             archivo.write(f'{estudiante.nombre},{estudiante.edad},{estudiante.carrera}\n')

    def listar_estudiantes(self):
        with open(self.nombre_archivo, 'r') as archivo:
            print('*** Listado de Estudiantes ***')
            for linea in archivo:
                print(linea.strip())

    def buscar_estudiante(self, nombre):
        try:
            encontrado = False
            with open(self.nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    if linea.startswith(nombre):
                        print('*** Información del Estudiante ***')
                        print(linea.strip())
                        encontrado = True
                        break
            if not encontrado:
                print('No se encontró ningún estudiante con ese nombre.')
        except Exception as e:
            print(f'Ocurrió un error al buscar el estudiante: {e}')

    def eliminar_registro_estudiantes(self):
        try:
            os.remove(self.nombre_archivo)
            print(f'Se ha eliminado el registro de estudiantes.')
        except Exception as e:
            print(f'Ocurrió un error al eliminar el registro de estudiantes: {e}')

print('*** Registro de Estudiantes ***')
opcion = None
registro_estudiantes = RegistroEstudiantes()
while opcion != 4:
    try:
        print('''Opciones:
        1. Agregar Estudiante
        2. Listar Estudiantes
        3. Buscar Estudiante
        4. Salir''')
        opcion = int(input('Escribe tu opción (1-4): '))
        if opcion == 1:  # Agregar estudiante
            nombre = input('Dame el nombre del estudiante: ')
            edad = input('Dame la edad del estudiante: ')
            carrera = input('Dame la carrera del estudiante: ')
            estudiante = Estudiante(nombre, edad, carrera)
            registro_estudiantes.agregar_estudiante(estudiante)
            print('Estudiante agregado correctamente.')
        elif opcion == 2:  # Listar estudiantes
            registro_estudiantes.listar_estudiantes()
        elif opcion == 3:  # Buscar estudiante
            nombre_buscar = input('Ingrese el nombre del estudiante que desea buscar: ')
            registro_estudiantes.buscar_estudiante(nombre_buscar)
        elif opcion == 4:  # Salir
            print('Saliendo del programa...')
        else:
            print('Opción inválida. Intente de nuevo.')
    except ValueError:
        print('Error: Por favor, ingresa un número del 1 al 4.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')
        opcion = None
