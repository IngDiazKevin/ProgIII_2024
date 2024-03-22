#Metodos para listas

lista  = [1, 2, 3, 4]
#Append AGREGA un elemento al final de la lista
lista.append(10)
print(lista[4])

#Sirve para VACIAR o LIMPIAR la lista
#Retorna una lista VACIA
lista.clear()
print("Lista despyes de CLEAR")
print(lista)

#Unir listas
lista_1 =[1,2,3]
lista_2 =[4,5,6]
#EXTEND une la lista1 con lista2
#EXTIENDE la lista 1
#La lista 2 no es modificada

lista_2.extend(lista_1)
print(lista_2)



#Eliminar un ELEMENTO DE  una LISTA
print(lista_1)
del lista_1[1]
print(lista_1)


#Count = Busca coincidencia dentro de sus ELEMENTOS
elementos = [1, 1, 0, 45, 5, 7 ,-9]
print(elementos.count(1))

#AGREGAR un elemento NUEVO EN UNA POSICION DADA
l = [1,2,3,5]
l.insert(  3 ,4)
l.insert(   5,"NUEVO ELEMENTO")
print(l)

#POP Eleiminar el ultimo elemento
l.pop()
print("Pop:", l)



nueva_lista = [10,20,30,20,40]
nueva_lista.remove(20)
nueva_lista.remove(20)
print(nueva_lista)

nueva_lista.reverse()

print("Retorno de REVERSE" ,nueva_lista)


n = ["a", "b", "c", "d","e" , "f","g","h"]
print(n[-1])

#REBANADAS
print("lista original:" , n)
n_lista = n[1:4] 
print("lista con rebanada", n_lista)



















