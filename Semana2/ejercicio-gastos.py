import json
import os

try:
    opcion = float(input("Ingrese (1) para consultar y (2) para agregar un gasto: "))
    if opcion == 1:
        IsConsulta = True
    elif opcion == 2:
        IsConsulta = False
    else:
        print("Opcion incorrecta")
        exit()
except ValueError:
    print("Error: eso no es un número")

ruta_archivo = "gastos.json"

if IsConsulta:
    #Al consultar mostrar el total por categoría
    if os.path.exists(ruta_archivo):
        # Leer archivo existente
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
         gastos = json.load(archivo)
         for gasto in gastos:
            print(f"{gasto['categoria']}: ${gasto['monto']:.2f}")
    else:
        print("Aún no ha ingresado ningun gasto")
else:
    #Pedir categoría y monto al usuario
    categoria = input("Ingrese categoría del gasto: ")

    try:
        monto = float(input("Ingrese monto del gasto: "))
    except ValueError:
        print("Error: eso no es un número")

    if os.path.exists(ruta_archivo):
        # Leer archivo existente
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            gastos = json.load(archivo)
    else:
        # Si no existe, crear lista vacía
        gastos = []

    # Buscar si ya existe la categoría
    categoria_encontrada = False

    for gasto in gastos:

        if gasto["categoria"].lower() == categoria.lower():
            gasto["monto"] += monto
            categoria_encontrada = True
            break

    # Si no existe, agregar nueva categoría
    if not categoria_encontrada:

        nuevo_gasto = {
            "categoria": categoria,
            "monto": monto
        }

        gastos.append(nuevo_gasto)

    # Guardar archivo actualizado
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, ensure_ascii=False, indent=4)

    print("Gasto guardado correctamente")

