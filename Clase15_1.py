#Metodo grind
#Crea casillas o tablas para los cuadros
#Permite mostrar imagen
#Y genera un diseño mas ordenado y evitamos usar pixeles

#sticky -> parametro
#N/S/W/E   - NW  - NE   - SW  - SE

#Padin
#Son los espacios alrededor de un elemento a los costados
#PADY y PADX

from tkinter import *

ventana = Tk()
ventana.geometry('630x360')
ventana.config(bg='#3CB371')

frame_1 = Frame(ventana, width=200, height=200, bg = '#2E8B57')
frame_1.pack()

#======= LABELs
label_1 = Label(frame_1, text= 'Nombre:')
label_1.grid(row = 0 , column=0, pady = 10, padx=10)

label_2 = Label(frame_1, text= 'Apellido:')
label_2.grid(row = 1 , column=0,  pady = 10, padx=10)

label_3 = Label(frame_1, text= 'Apellido:')
label_3.grid(row = 2 , column=0,  pady = 10, padx=10)

#======= Campos de texto

texto_1 = Entry(frame_1)
texto_1.grid(row = 0, column=1, pady = 10, padx=10)

texto_2 = Entry(frame_1)
texto_2.grid(row = 1 , column=1, pady = 10, padx=10)

texto_3 = Entry(frame_1)
texto_3.grid(row = 2 , column=1, pady = 10, padx=10)

ventana.mainloop()

