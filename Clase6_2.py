class Inventario:
    def __init__(self):
        self.elementos = []
    
    def agregar_elemento(self , elemento):
        self.elementos.append(elemento)
        print(f"Elemento '{elemento}' fue agregado")
    
    def eliminar_elemento(self, elemento):
        if elemento in self.elementos:
           self.elementos.remove(elemento)
           print("El elemento fue eliminado con exito")
        else:
            print("EL elemento no fue eliminado porque no existe")
    
    def buscar_elemento(self,elemento):
        if elemento in self.elementos:
            print("EL elemento se encontro en la lista")
        else:
            print("El elemento no existe en la lsita")
    
    def mostrar_inventario(self):
        print("----INVENTARIO ----")
        for i in self.elementos:
            print(i)
    

#Crear una instancio (OBJETO) de la clase Inventario
mi_primer_inventario = Inventario()

#Agregando elementos al Inventario
mi_primer_inventario.agregar_elemento("Espada")
mi_primer_inventario.agregar_elemento("Pocion")
mi_primer_inventario.agregar_elemento("Escudo")
mi_primer_inventario.agregar_elemento("Armadura")

#Mostrar mi inventario
mi_primer_inventario.mostrar_inventario()

#Buscar elementos
mi_primer_inventario.buscar_elemento("Escudo")
mi_primer_inventario.buscar_elemento("Salchicha")

#Eliminamos elemetos del inventario
mi_primer_inventario.eliminar_elemento("Silla")
mi_primer_inventario.eliminar_elemento("Pocion")
mi_primer_inventario.eliminar_elemento("Espada")
mi_primer_inventario.eliminar_elemento("Escudo")
mi_primer_inventario.eliminar_elemento("Armadura")

#Mostrar mi inventario
mi_primer_inventario.mostrar_inventario()
















    
    
            
        
        
       
        