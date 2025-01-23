productos = {"manzana": 1.5, "banana": 0.8, "leche": 2.3}
producto2 = {}
for producto, precios in productos.items():
    if precios > 1:
        producto2[producto]=precios
print(producto2)  