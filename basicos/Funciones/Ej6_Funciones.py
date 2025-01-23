def promedio(*args):
    suma = 0
    for n in args:
        suma = suma + n
        promedio = suma / len(args)
    return promedio

print(promedio(8,8,9,10,10,10,10))
print(promedio(5, 19,173,2,35))
print(promedio(7,45,20,87,36))