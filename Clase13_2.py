#Diseño de ventanas
from tkinter import * # el asterisco me sirve para indicar que importare 
                     # TODA  la libreria TINKTER

#Instanciar o CREAR EL OBJETO
ventana = Tk()                            #creando el objeto "ventana" de la clase TK
ventana.title('Mi primer ventana con TK')
ventana.iconbitmap('GATO.ico') #archivo con extension .ico para el ICONO de la ventana
ventana.geometry('680x400') #Recibe una cada con el ancho y largo en pixeles de la ventana

frame_1 = Frame()
    
#Tres posibles opciones:
frame_1.pack(side = 'left', anchor= 'n')  #Empaquetando frame_1 para que sea visible
#frame_1.place(x = 500, y = 10)
#frame_1.grid(row=1,column=2)

frame_1.config(width= 200, height= 250) #El tamaño del frame o contenedor en pixeles
frame_1.config(bg = '#EBDD23', bd =25)
frame_1.config(relief = 'sunken') #Variaciones = flat, sunken, raised, ridge
frame_1.config(cursor= 'pirate') #Cambiar el tipo de cursor EN EL FRAME
                                 #Variaciones = arrow, circle, cross, dot, fleur, 
                                 #heart, man, mouse, plus, shuttle, spider, star, etc
                
ventana.mainloop() #mainloop mantiene la ventan abierta (bucle)







