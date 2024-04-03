#Anexar archivos

archivo = open('mi_archivo.txt','a')

for i in range(0,3):
    archivo.write('Estoy anexando\n')
archivo.write('Adios\n')

archivo.close()


