diccionario = {
    "nombre" : "perro",
    "apellido" : "gato",
    "sub" : 1000
    
}

# devuelve las claves
claves = diccionario.keys()

# devuelve el valor dado
claves = diccionario.get("sub")

#eliminar un elemento del diccionario
diccionario.pop("sub")

#eliminado un elemento dict_items iterable
dic_iterable = diccionario.items()

#eliminando el diccionario
# diccionario.clear()

print(dic_iterable)