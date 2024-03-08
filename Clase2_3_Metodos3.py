#Metodos3
class Galletas:
      chocolate = False
      sabor = None
      color = None
      forma = "Cuadrado"
      
      def __init__(self,sabor, color):
            self.sabor = sabor
            self.color = color
            print("Se creo una galleta")
      
      def a_chocolate(self):
            self.chocolate = True
            
galletita = Galletas("salado","naranja")
galletita.a_chocolate()

print(galletita)