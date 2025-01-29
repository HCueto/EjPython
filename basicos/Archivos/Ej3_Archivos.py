palabra_buscada = input("Introduce la palabra a buscar: ")
contador = 0

with open("Archivos/articulo.txt", "r") as archivo:
    for linea in archivo:
        contador += linea.lower().count(palabra_buscada.lower())
print(f'La palabra {palabra_buscada} sale un total de {contador} veces en el articulo.')