#Scrooll bar
#Campo de texto a nivel de widget
#permite agregar mucho texto

#scrollbar
#ayuda a ubicarnos delizando y ver frames amplios
#YVIEM 
#sticky = nsew ajustar al tamaño del frame
#YCSCROLLCOMMAND

from tkinter import *

ventana = Tk()
ventana.geometry('630x360')
ventana.config(bg = 'black')

frame_1 = Frame(ventana)
frame_1.pack()

campotexto_1 = Text(frame_1)
campotexto_1.grid(row=0,column=0)

#extra  colores y tamño
campotexto_1.config(width =40 , height=10)
campotexto_1.config(bg = 'cyan', fg = 'green', fon = ('Arial',20) )

#Diseño scrollbar
#scroll_1 = Scrollbar(frame_1)
scroll_1 = Scrollbar(frame_1, command= campotexto_1.yview)
#scroll_1.grid(row=0, column=1)

#No funciona, agregar a nuestro campo de texto
#reemplazar la linea 27 por:
#scroll_1 = Scrollbar(frame_1, command= campotexto_1.yview)

#Modificar el grind - linea 29
scroll_1.grid(row=0, column=1, sticky= 'nesw')

#extra hacer que el scrool se mueva
campotexto_1.config(yscrollcommand= scroll_1.set)

ventana.mainloop()
