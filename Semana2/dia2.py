with open("Semana2/notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera línea con tildes: á é í ó ú\n")
    archivo.write("Segunda línea: ñ ü\n")

print("Archivo creado")

# leer todo el archivo de una vez
with open("Semana2/notas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

# leer línea por línea
with open("Semana2/notas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())

# "w" → escribe, si el archivo existe lo BORRA y empieza de cero
with open("Semana2/notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Línea nueva\n")

# "a" → append, agrega al final sin borrar lo que había
with open("Semana2/notas.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Línea agregada\n")

# "r" → solo lectura, no puede modificar
with open("Semana2/notas.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())