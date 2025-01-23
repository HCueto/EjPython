productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}
total = 0
for producto, precios in productos.items():
    total = total + precios
print(f'El precio total es {total}')