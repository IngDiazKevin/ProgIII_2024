#Campos de texto
#Entry
#Agregar o excribir informacion

from tkinter import *

#Ventana
ventana = Tk()
ventana.geometry('630x360')

#Frame u organizador
frame_1 = Frame(ventana, width= '600', height='330')
frame_1.place(x = 10, y = 10)
frame_1.config(bg = 'green')

#Campo de texto
texto_1 = Entry(frame_1)  #Pertenece a frame 1
texto_1.pack()      #empaquetado en frame 1
texto_1.config(font = ('arial black', 16))
texto_1.config(bg = 'blue', fg = 'red')

def imprimir():
    label_1 = Label(frame_1, text = (texto_1.get(), texto_1.index(ANCHOR)))
    label_1.pack()
    #Configurar el label
    label_1.config(bg = 'cyan')
    label_1.config(fb = 'gren')
    label_1.config(font = ('consolas', 20))
    
btn_1 = Button(frame_1, text= 'Imprimir', command = imprimir)
btn_1.pack()

ventana.mainloop()