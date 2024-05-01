#Menus

from tkinter import *
ventana = Tk()

#Crear el espacio del menu
menuBar = Menu(ventana)
ventana.config(menu = menuBar) #Agrego el menu como MENU a la ventana

#----------------Pestaña
pestana_1 = Menu(menuBar, tearoff= 0)
menuBar.add_cascade(label='Archivo', menu= pestana_1)


pestana_2 = Menu(menuBar, tearoff= 0)
menuBar.add_cascade(label='Editar', menu= pestana_2)

pestana_3 = Menu(menuBar, tearoff= 0)
menuBar.add_cascade(label='Seleccion', menu= pestana_3)

ventana.mainloop()
