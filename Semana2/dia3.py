import json

# datos en un diccionario
persona = {
    "nombre": "Fede",
    "edad": 30,
    "habilidades": ["GeneXus", "Python"],
    "activo": True
}

with open("Semana2/persona.json", "w", encoding="utf-8") as archivo:
    json.dump(persona, archivo, ensure_ascii=False, indent=4)

print ("JSON guardado")

# leer el JSON
with open("Semana2/persona.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print(datos)
print(type(datos))  # fijate que es un diccionario
print(datos["nombre"])
print(datos["habilidades"][0])