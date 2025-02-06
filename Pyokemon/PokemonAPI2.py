import requests
import tkinter
def pokemonFunc():
    pokemon = cajaTexto.get()
    url = (f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    response = requests.get(url)
#with open(f"{pokemon}.json","w") as data :
    data = response.json()

#with open(f"{pokemon}.json","r") as pokemon:
    #datos_diccionario = json.loads(pokemon)

    nombre = data['name']
    id = data['id']
    tipos = data['types']
    rango = range(len(tipos)) 
    tipo = []
    for i in rango:
        tipo.append( data["types"][i]["type"]["name"])
    tipof = ', '.join(tipo)
    altura = data['height']
    peso = data['weight']
#tipo=tipos('type')
    print('------------------------')
    print(f"Nombre: {nombre}")
    print(f"ID: {id}")
    print(f"Tipo/s: {tipof}")
    print(f"Altura: {altura}")
    print(f"Peso: {peso}")
    print('------------------------')
    etiqueta2["text"] = nombre
    etiqueta3["text"] = id
    etiqueta4["text"] = tipof
    etiqueta5["text"] = altura
    etiqueta6["text"] = peso

ventana = tkinter.Tk()
ventana.geometry("400x400")

etiqueta = tkinter.Label(ventana, text = "Pyokemon", bg = "green")
etiqueta.grid()

cajaTexto = tkinter.Entry(ventana)
cajaTexto.grid(row=0,column=0)

button1 = tkinter.Button(ventana, text = "Enviar", command = pokemonFunc)
button1.grid(row=0,column=1)

etiqueta2A = tkinter.Label(ventana, text = "Nombre", bg = "blue")
etiqueta2A.grid(row=1,column=0)

etiqueta2 = tkinter.Label()
etiqueta2.grid(row=1,column=1)

etiqueta3A = tkinter.Label(ventana, text = "ID", bg = "blue")
etiqueta3A.grid(row=2,column=0)

etiqueta3 = tkinter.Label()
etiqueta3.grid(row=2,column=1)

etiqueta4A = tkinter.Label(ventana, text = "Tipos", bg = "blue")
etiqueta4A.grid(row=3,column=0)

etiqueta4 = tkinter.Label()
etiqueta4.grid(row=3,column=1)

etiqueta5A = tkinter.Label(ventana, text = "Altura", bg = "blue")
etiqueta5A.grid(row=4,column=0)

etiqueta5 = tkinter.Label()
etiqueta5.grid(row=4,column=1)

etiqueta6A = tkinter.Label(ventana, text = "Peso", bg = "blue")
etiqueta6A.grid(row=5,column=0)

etiqueta6 = tkinter.Label()
etiqueta6.grid(row=5,column=1)

ventana.mainloop()