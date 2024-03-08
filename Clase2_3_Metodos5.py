#Metodos5
class Galletas:
      chocolate = False
      sabor = None
      color = None
      forma = "Cuadrado"
      
      def __init__(self,sabor = None, color = None):
            
            self.sabor = sabor
            self.color = color
            if sabor is not None and color is not None:
                  print("Se creo una galleta {} de sabor {}".format(sabor,color))
                  
      
      def a_chocolate(self):
            self.chocolate = True
            
galletita = Galletas()
galletita.a_chocolate()

print(galletita)