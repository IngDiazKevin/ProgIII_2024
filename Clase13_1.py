#Diseño de ventanas
from tkinter import * # el asterisco me sirve para indicar que importare 
                     # TODA  la libreria TINKTER

#Instanciar o CREAR EL OBJETO
ventana = Tk()                            #creando el objeto "ventana" de la clase TK
ventana.title('Mi primer ventana con TK')
ventana.iconbitmap('GATO.ico') #archivo con extension .ico para el ICONO de la ventana
ventana.geometry('680x400') #Recibe una cada con el ancho y largo en pixeles de la ventana
ventana.config(bg  = '#BF7ACF')  #bg = background = fondo 
ventana.resizable(True,True)    #No se puede modifcar el ancho ni el largo
                                #EL primero es el ancho
                                #El segundo es el largo


ventana.mainloop() #mainloop mantiene la ventan abierta (bucle)







