def imprimir_detalles(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
imprimir_detalles(marca='Audi',modelo='A6',color='Negro')