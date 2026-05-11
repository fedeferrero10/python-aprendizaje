# sin manejo de errores - esto rompe
try:
    numero = int(input("Ingresá un número: "))
    print(f"El doble es: {numero * 2}")
except ValueError:
    print("Error: eso no es un número")
finally:
    print("Esto se ejecuta siempre")

try:
    numero = int(input("Ingresá un número: "))
    resultado = 100 / numero
    print(f"100 dividido {numero} es: {resultado}")
except ValueError:
    print("Error: eso no es un número")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
finally:
    print("Fin del programa")