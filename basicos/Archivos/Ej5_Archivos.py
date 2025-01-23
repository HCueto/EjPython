with open("Archivos/origen.txt", "r") as origen:
    contenido = origen.read()
with open("Archivos/destino.txt", "w") as destino:
    destino.write(contenido)

print(f'Se ha creado la copia en destino.txt.')