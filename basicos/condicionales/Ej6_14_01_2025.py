letra = input("Dame una letra: ")
vocal = ["a","e","i","o","u"]
if len(letra) == 1:
    if letra in vocal:
        print("La letra es una vocal.")
    else:
        print("No es una vocal")
else:
    print("Eso no es una sola letra, intentalo de nuevo.")