class Inventario:
    def __init__(self):
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)
        print(f"Elemento '{elemento}' agregado al inventario.")

    def eliminar_elemento(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
            print(f"Elemento '{elemento}' eliminado del inventario.")
        else:
            print(f"El elemento '{elemento}' no está en el inventario.")

    def buscar_elemento(self, elemento):
        if elemento in self.elementos:
            print(f"El elemento '{elemento}' está en el inventario.")
        else:
            print(f"El elemento '{elemento}' no está en el inventario.")

    def mostrar_inventario(self):
        print("Inventario:")
        for elemento in self.elementos:
            print("-", elemento)


# Crear una instancia de la clase Inventario
mi_inventario = Inventario()

# Agregar elementos al inventario
mi_inventario.agregar_elemento("Espada")
mi_inventario.agregar_elemento("Poción")
mi_inventario.agregar_elemento("Armadura")

# Mostrar el inventario
mi_inventario.mostrar_inventario()

# Buscar un elemento en el inventario
mi_inventario.buscar_elemento("Espada")
mi_inventario.buscar_elemento("Gema")

# Eliminar un elemento del inventario
mi_inventario.eliminar_elemento("Poción")
mi_inventario.eliminar_elemento("Gema")  # Intentar eliminar un elemento que no está en el inventario