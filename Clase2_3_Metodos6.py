#Metodos6
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
      
      def tiene_chocolate(self):
            if(self.chocolate):
                  print("Soy una galleta con chocolate")
            else:
                  print("Soy una galleta SIN chocolate")            
galletita = Galletas()
galletita.tiene_chocolate()
galletita.a_chocolate()
galletita.tiene_chocolate()
print(galletita)