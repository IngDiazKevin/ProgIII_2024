#Ejercicio
#1. Implementa una función llamada crear_archivo que tome el nombre del archivo como
#   argumento y verifique si el archivo ya existe. Si no existe, crea el archivo.
#   Si ya existe, muestra un mensaje indicando que el archivo ya existe.

#2. Implementa una función llamada agregar_estudiante que tome el nombre del archivo
#   como argumento. Esta función debe solicitar al usuario ingresar el nombre,
#   la edad y el curso del estudiante, y luego agregar esta información al archivo
#   en el formato: "nombre,edad,curso".

#3. Implementa una función llamada mostrar_estudiantes que tome el nombre del archivo
#   como argumento. Esta función debe abrir el archivo en modo lectura y mostrar la
#   información de todos los estudiantes registrados en el archivo.

#4. Crea un archivo llamado "estudiantes.txt" si no existe al inicio del programa.

#5. Utiliza un bucle para mostrar un menú al usuario con las siguientes opciones:

#  Opción 1: Agregar información de estudiante
#  Opción 2: Mostrar todos los estudiantes
#  Opción 3: Salir del programa
#Implementa la lógica para ejecutar la opción seleccionada por el usuario en el menú.



import os
def crear_archivo(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'x'): #with junto con el OPEN = habilitan el archivo
            print(f'Se creo el archivo {nombre_archivo}')
    else:
        print(f'El archvo {nombre_archivo} ya existe')
        
def agregar_estudiante(nombre_archivo):
    nombre = input('Ingres el nombre: ')
    edad = input('Ingrese la edad: ')
    curso = input('Ingres el curso: ') 
    
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(f'{nombre},{edad},{curso}\n') #Observacion
    print('Informacion del estudiante se agrego correctamente')

def mostrar_estudiantes(nombre_archivo):
    print('*** Lista de estudiantes ***')
    with open(nombre_archivo, 'r') as archivo:
        print(archivo.read())
    
nombre_archivo = 'estudiantes2.txt'

crear_archivo(nombre_archivo)

while True:
    print('\n **** --- MENU --- ***')
    print('1 - Agregar estudiantes')
    print('2 - Mostrar Estudiantes')
    print('Salir')
    
    opcion = input('Seleccione una opcion: ')
    
    if opcion == '1':
        agregar_estudiante(nombre_archivo)
    elif opcion == '2':
        mostrar_estudiantes(nombre_archivo)
    elif opcion == '3':
        break
    else:
        print('Opcion no valida, por favor seleccione una opcion valida')
        


    


    