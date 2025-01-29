
contador = 0
with open("Archivos/poema.txt", "r") as poema:
    for linea in poema:
        linea.strip() 
        contador = contador + 1
print(f'Tiene {contador} lineas.')