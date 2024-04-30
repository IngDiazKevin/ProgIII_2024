#Radio button
#Los radio button permiten versatilidad para marchar o
#desmarcar opciones predeterminadas

from tkinter import *

ventana = Tk()
ventana.geometry('640x360')

opcion = IntVar()

radio_btn1 = Radiobutton(ventana, text='Opcion 1')
radio_btn1.pack()
radio_btn1.config(variable=opcion, value=1) 

radio_btn2 = Radiobutton(ventana, text='Opcion 2')
radio_btn2.pack()
radio_btn2.config(variable=opcion, value=2) 

radio_btn3 = Radiobutton(ventana, text='Opcion 3')
radio_btn3.pack()
radio_btn3.config(variable=opcion, value=3) 

label_1 = Label(ventana)
label_1.pack()

ventana.mainloop()