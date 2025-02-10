import requests

pokemon = input('Introduzca el pokemon que quieras: ')
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