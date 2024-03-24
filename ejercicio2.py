# le pedimos al usuario que nos diga una frase 
frase = input("dime una frace y de calculo cuanto tardarias en decirla")

#creamos una lista con todas las palabras (separadas por espacio)
palabras_separadas = frase.split(" ")

# contamos la cantidad de elementos
cantidad_palabras = len(palabras_separadas)

#si tarda mas de un minuto pedimos que pare
if cantidad_palabras > 120 :
    print("Parar")
    
#calculamos cuanto tardaria en decirlo
print(f'Dijiste {cantidad_palabras} palabras, y tardarias { cantidad_palabras/2} segundos en decirlo')
print(f'Dalto lo diria en {cantidad_palabras * 100 // 2 * 1.3 / 100} segundos')    