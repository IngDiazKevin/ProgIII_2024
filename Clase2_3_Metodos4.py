#Metodos4
class Galletas:
      chocolate = False
      sabor = None
      color = None
      forma = "Cuadrado"
      
      def __init__(self,sabor = None, color = None):
            self.sabor = sabor
            self.color = color
            print("Se creo una galleta {} de sabor {}".format(sabor,color))
      
      def a_chocolate(self):
            self.chocolate = True
            
galletita = Galletas("salada","naranja")
galletita.a_chocolate()

print(galletita)