# metodos de cadena

# sintaxis - dato.metodo()

cadena1 = "Hola Dalto"
cadena2 = "Bienvenido Mam"
cadena3 = "a"

# Devuelve la lista de atributos validos del objeto pasado
dir(cadena1)

#convierte a mayuscula
resultado = cadena1.upper()

#convierte a minuscula
resultado = cadena1.lower()

#convierte primera letra mayuscula
resultado = cadena1.capitalize()

#Busca cadena en otra cadena/ devuelve la posicion donde se encuentra el valor, si no encuentra resultado devuelve -1
busqueda_find = cadena1.find("a")

# Busca cadena en otra cadena/ si no hay coincidencias lanza una exception
busqueda_index = cadena1.index("D")

# si es numerico, devuelve true, si no devuelve false
es_numerico = cadena3.isnumeric()

# si es alfanumerico devuelve true, solo letra
es_alfanumeric = cadena3.isalpha()

# Busca cadena en otra cadena/ devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("a")

# contamos cuantos caracteres tiene una cadena/ es una funcion
contar_caracteres = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("Hol")

# verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("to")

# reemplaza una parte de la cadena
cadena_nueva = cadena1.replace("Hola", "perro")

# separa cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(" ")


print(cadena_separada)


