"""
Un profesor tiene una lista de útiles escolares y quiere saber cuáles están en "bajo stock". Los estudiantes deben procesar 
una lista de productos y filtrar solo aquellos que tienen pocas unidades para lanzar una alerta.
Detalles técnicos requeridos:
•	Estructura de datos: Crear una lista de diccionarios, donde cada diccionario tenga nombre y cantidad.
{“nombre”:”cuadernos” , “cantidad”:12}
{“nombre”:”cuadernos” , “cantidad”:4}
{“nombre”:”cuadernos” , “cantidad”:10}

•	Bucle: Usar un for para recorrer la lista de productos.
•	Lógica: Si la cantidad es menor a 5, mostrar un mensaje de "ALERTA: Reponer [nombre]".
•	Extra: Al final del programa, mostrar cuántos productos totales se revisaron usando la función len().

"""
"""
import csv
productos = [
    {"nombre": "cuadernos", "cantidad": 12},
    {"nombre": "lápices", "cantidad": 4},
    {"nombre": "borradores", "cantidad": 10},
    {"nombre": "colores", "cantidad": 3},
    {"nombre": "reglas", "cantidad": 7} ] """

import csv
import os

productos = []

if os.path.exists("productos.csv"):
    with open("productos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            productos.append({
                "nombre": fila["nombre"],
                "cantidad": int(fila["cantidad"])
            })
else:
    productos = [
        {"nombre": "cuadernos", "cantidad": 12},
        {"nombre": "lápices", "cantidad": 4},
        {"nombre": "borradores", "cantidad": 10},
        {"nombre": "colores", "cantidad": 3},
        {"nombre": "reglas", "cantidad": 7}
    ]


retirar_productos = input(f"Nombre del producto a retirar: ")
cantidad_retirar = int(input(f"Cantidad a retirar: "))

for producto in productos:
    if producto["nombre"] == retirar_productos:
        if producto["cantidad"] >= cantidad_retirar:
            producto["cantidad"] -= cantidad_retirar
        else:
            print("No hay suficiente stock.")

for producto in productos:
    if producto["cantidad"] < 5:
        print(f"ALERTA: Reponer {producto['nombre']}")

print(f"Productos totales revisados: {len(productos)}") 


# Guardar en CSV
with open("productos.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "cantidad"])
    for producto in productos:
        escritor.writerow([producto["nombre"], producto["cantidad"]])

print("Datos guardados en productos.csv")