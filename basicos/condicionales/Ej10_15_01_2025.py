precio=int(input('Dame el precio del producto: '))
if precio >= 1000:
    precioF=precio-(precio*(10/100))
    print(f'Su precio final es {precioF}')
else:
    print(f'Su precio final es {precio}')