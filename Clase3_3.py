#HERENCIA

class Producto:
      def __init__(self, codigo, nombre, precio, descripcion):
            self.codigo = codigo
            self.nombre = nombre
            self.precio = precio
            self.descripcion = descripcion
            
      def __str__(self):
            return f"Codigo\t\t{self.codigo}\n"\
                   f"Nombre\t\t{self.nombre}\n"\
                   f"Precio\t\t{self.precio}\n"\
                   f"Descripcion\t{self.descripcion}\n"    
            
class libro(Producto):
      pass

libro_1 = libro(1234, "Coquito", "35", "Inicial primaria" )
print(libro_1)
