#Uso de check button 1/3
from tkinter import *

ventana = Tk()
ventana.geometry('630x420')
ventana.config(bg = 'green')

valor1 = IntVar()
valor2 = IntVar()

def selecionar():
    cadena = ''

    if (valor1.get()):
        cadena = cadena + 'Check btn 1 Marcado'
    else:
        cadena = cadena + 'Check btn 1 Desmarcado'
    
    if (valor2.get()):
        cadena = cadena + ' & Check btn 2 Marcado'
    else:
        cadena = cadena + '& Check btn 2 Desmarcado'
    
    #Mostrar la info en el label
    label1.config(text = cadena)
    label1.config(bg = 'cyan')

chek_btn1 = Checkbutton(ventana, variable= valor1, text = 'Boton 1' , onvalue= 1 , offvalue=0, command= selecionar)
chek_btn2 = Checkbutton(ventana, variable= valor2, text = 'Boton 2' , onvalue= 1 , offvalue=0, command= selecionar)
chek_btn1.pack()
chek_btn2.pack()

label1 = Label(ventana)
label1.pack()

ventana.mainloop()