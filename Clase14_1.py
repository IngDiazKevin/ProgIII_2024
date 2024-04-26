#Botones
#Es una parte de una interfaz que al hacer click genera una accion
#Para que esta accion se ejecute debe estar de la mano de una funcion

from tkinter import *

def saludo():
    label_1 = Label(frame_1, text = 'Hola programacion III')
    label_1.place(x= 250, y = 20)
    
#Crear la ventana
ventana = Tk()
ventana.geometry('800x600')

#Crear frame o contenedor
frame_1 = Frame(ventana, width='780' , height= '580')
frame_1.config(bg = 'green')
frame_1.place(x = 10, y = 10)

btn_1 = Button(frame_1, text = 'Saludar', command = saludo) #command es la accion del btn
btn_1.place(x=10,y=10)
btn_1.config(bg = 'red', fg = 'blue') #bg para el fondo, fg para el color de la letra
btn_1.config(fon = ('arial',26))   #fon = tipo de letras y tamaño
btn_1.config(cursor= 'heart') #Cambia el curso cuando este sobre el boton

imagen_1 = PhotoImage(file = 'fondo_tecba.png') 

btn_2 = Button(frame_1, image = imagen_1)
btn_2.place(x = 10, y = 100)

ventana.mainloop()