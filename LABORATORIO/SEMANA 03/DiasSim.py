
import random 
def dias_clima(cantidad):
    for i in range(cantidad):
         clima = random.choice(["soleado","nublado","lluvioso"])
         print(f"Dia {i+1} sera: {clima}")

try:
    ingreso_usuario = int(input("Ingrese la cantidad de dias a predecir:"))
    dias_clima(ingreso_usuario)
except ValueError:
    print("Error: Por favor, ingresa un número entero válido")
