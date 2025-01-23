num = int(input("Elija un numero entre 1 y 7: "))
if num >= 1 and num <= 7:
    if num == 1:
        print(f"{num}: Lunes.")
    elif num == 2:
        print(f"{num}: Martes.")
    elif num == 3:
        print(f"{num}: Miercoles.")
    elif num == 4:
        print(f"{num}: Jueves.")
    elif num == 5:
        print(f"{num}: Viernes.")
    elif num == 6:
        print(f"{num}: Sabado.")
    elif num == 7:
        print(f"{num}: Domingo.")
else:
    print(f"{num} esta fuera del rango.")