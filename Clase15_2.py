#Crear un campo de texto que pid
# usuario y Contraseña (****)
#btn aceptar

#Show -> oculta espacios como las contraseñas y reemplaza los caracteres por (***)

#justify utiliza las expresiones left, center y right para
#q el texto que ingresemos se ubique de acuerdo a lo que contiene justify

#Columnspan une columans para un solo elemento

#Funciones QUIT y exit
#quit la actual
#exit todas

from tkinter import *

ventana = Tk()
ventana.geometry('630x360')
ventana.config(bg='#3CB371')

frame_1 = Frame(ventana, width=200, height=200, bg = '#2E8B57')
frame_1.pack()

#======= LABELs
label_user = Label(frame_1, text= 'Usuario:')
label_user.grid(row = 0 , column=0, pady = 10, padx=10)

label_contra = Label(frame_1, text= 'Contraseña:')
label_contra.grid(row = 1 , column=0,  pady = 10, padx=10)



#======= Campos de texto

texto_user = Entry(frame_1, justify= 'center')  #Right y lefth
texto_user.grid(row = 0, column=1, pady = 10, padx=10)

texto_contra = Entry(frame_1, show= '*')
texto_contra.grid(row = 1 , column=1, pady = 10, padx=10)

btn_aceptar =  Button(frame_1, text='Aceptar', command= quit)
btn_aceptar.grid(row=2, column=0, padx=10,pady=10, columnspan=2)
#btn_aceptar.config(width = 20)
ventana.mainloop()
