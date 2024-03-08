#Metodos
class Galletas:
      chocolate = False
      sabor = None
      color = None
      forma = "Cuadrado"
      
      def __init__(self):
            print("Se creo una galleta")
      
      def a_chocolate(self):
            self.chocolate = True
            
galletita = Galletas()
print(galletita.chocolate)