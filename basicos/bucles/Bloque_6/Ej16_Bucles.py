contrasena_correcta = "python123"
contrasena = ""
while contrasena != contrasena_correcta:
    contrasena=input("Introduzca su contraseña:")
    if  contrasena != contrasena_correcta:
        print('Contraseña incorrecta escriba de nuevo.')
else:
    print('Feicidades a puesto la contraseña correcta.')