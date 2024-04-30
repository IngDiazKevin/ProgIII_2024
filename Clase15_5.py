#Radio button 

from tkinter import *

ventana = Tk()
ventana.geometry('640x360')

opcion = IntVar()
#agregar
def seleccionado():
    label_1.config(text = opcion.get())

#agregar command
radio_btn1 = Radiobutton(ventana, text='Opcion 1',command = seleccionado)
radio_btn1.pack()
radio_btn1.config(variable=opcion, value=1) 

radio_btn2 = Radiobutton(ventana, text='Opcion 2',command = seleccionado)
radio_btn2.pack()
radio_btn2.config(variable=opcion, value=2) 

radio_btn3 = Radiobutton(ventana, text='Opcion 3',command = seleccionado)
radio_btn3.pack()
radio_btn3.config(variable=opcion, value=3) 

label_1 = Label(ventana)
label_1.pack()

#extra

def reiniciar():
    opcion.set(None)
    label_1.config(text = '')

btn_1 = Button(ventana, text='Limpiar', command=reiniciar).pack()

ventana.mainloop()