
"""
Diseña un programa que permita calcular 
el área de un círculo o el volumen de una esfera utilizando 
el módulo math.
1: Crea una función para el área del círculo.
2: Crea una función para el volumen de la esfera 
3: Usa math.pi para obtener el valor preciso de Pi(3.1416...)
4: Solicita al usuario el radio y la opción deseada.
"""
import math

def area_circulo(radio):
    return math.pi*math.pow(radio,2)

def volumen_esfera(radio):
    return (4/3)*math.pi*(radio**3)

print("1. Área Círculo")
print("2. Volumen Esfera")

opcion = int(input("Ingrese la opcion deseada: "))
r = float(input("Ingrese el radio: "))

if opcion == 1:
    print(f"El área del círculo es: {area_circulo(r):.2f}")
elif opcion == 2:
    print(f"El volumen de la esfera es: {volumen_esfera(r):.2f}")
else:
    print("Opción no válida")