#Escribir una lista de datos en un archivo

nombre_archivo = 'mi_archivo.txt'

#lista = ['Jupiter\n', 'Martes\n', 'Venus\n']

#with open(nombre_archivo, 'a+') as archivo: # a+ = modo especial = anexar + escribir
#    archivo.writelines(lista)
#print('Se anexo una nueva lista')

#ELiminar archivos

import os

if os.path.exists(nombre_archivo):
    os.remove(nombre_archivo)
    print("Se ha eliminado")
else:
    print("El archivo no existe por tal razon NO SE ELIMINO NADA")


