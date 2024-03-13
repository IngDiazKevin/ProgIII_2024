#Encapsulamiento
class Ejemplo:
      __atributo_privado = "Soy un atributo PRIVADO"
      
      def __metodo_privado(self):
            print("Soy un Metodo PRIVADO")
            
      def atributo_publico(self):
            return self.__atributo_privado
      
      def metodo_publico(self):
            return self.__metodo_privado()
      
objecto = Ejemplo()
#print(objecto.__atributo_privado)
print(objecto.atributo_publico())





