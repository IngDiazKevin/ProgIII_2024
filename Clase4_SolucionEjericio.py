class Producto:
  def __init__(self,codigo, nombre, precio, descripcion):
    self.codigo = codigo
    self.nombre = nombre
    self.precio = precio
    self.descripcion = descripcion

  def __str__(self):
    return f"Codigo:\t\t{self.codigo}\n"\
           f"Nombre:\t\t{self.nombre}\n"\
           f"Precio:\t\t{self.precio} bs\n"\
           f"Descripcion:\t{self.descripcion}\n"

class libro(Producto):
  pass

class alimento(Producto):
  productor = ""
  distribuidor = ""

  def __str__(self):
    return f"Codigo:\t\t{self.codigo}\n"\
           f"Nombre:\t\t{self.nombre}\n"\
           f"Precio:\t\t{self.precio} bs\n"\
           f"Descripcion:\t{self.descripcion}\n"\
           f"Productor:\t{self.productor}\n"\
           f"Distribuidor:\t{self.distribuidor}\n"

libro_1 = libro(1234, "Harry Potter", "200", "Primera edicion")
#print(libro_1)

alimento_1 = alimento(5678, "Soda" , "15", "2 litros")
alimento_1.productor = "CocaColaCompany"
alimento_1.distribuidor = "EMBOL"
print(alimento_1)
