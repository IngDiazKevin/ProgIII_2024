#Objeto puede estar dentro de otro objeto

class pelicula:
      def __init__ (self, titulo, duracion, lanzamiento):
            self.titulo = titulo
            self.duracion = duracion
            self.lanzamiento = lanzamiento
            
            print("Se creo la pelicula" , self.titulo)
            
      def __str__(self): #Servira para imprimir un mensaje
            return "{} lanzado en {} con una duracion de {} min".format(self.titulo, self.lanzamiento , self.duracion)       
            
class catalogo:
      peliculas = []
      
      def __init__(self, peliculas=[]):
            self.peliculas = peliculas
            
      def mostrar(self):
            for p in self.peliculas:
                  print(p)

a = pelicula("Harry Potter", 175 , 1972)
c = catalogo([a])
c.mostrar
            
            
            

            