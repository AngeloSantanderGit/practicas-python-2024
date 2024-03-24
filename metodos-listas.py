# crear una lista
#lista = list(["hola", "perro", 35, 20, True])
lista = list([53, 35, 20, True])

# devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

# agregando elementos a la lista
lista.append(65)

# agregando un elemtento a la lista en un indice epecifico
lista.insert(2,8)

# agregamos varios elementos
lista.extend([False, 2030])

#eliminando un elemento de la lista (por su indice)
lista.pop(-1)

# remover un elemento de la lista por su valor
lista.remove(35)

# elimina todos los elementos de la lista 
#lista.clear()

# ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa) solo elementos numericos
lista.sort()

#invirtiendo los elemtos de una lista
lista.reverse()




print(lista)

print(dir(lista))

