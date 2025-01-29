nombres = ["Ana", "Luis", "Pedro", "María", "Laura", "Raul"]

with open("Archivos/nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")

print("Los nombres se han guardado en 'nombres.txt'.")