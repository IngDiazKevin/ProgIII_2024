#Metodos2
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
galletita.a_chocolate()
print(galletita)