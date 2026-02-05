"""
🧠 Objetivo

Pedir al usuario cuántas veces lanzar una moneda

Cada lanzamiento da Cara o Sello

Usar try/except solo donde puede fallar

Usar función + bucle
"""

import random

def lanzar_moneda(veces):
    for i in range(veces):
        lanzamiento = random.choice(["cara","sello"])
        print(f"Lanzamiento {i+1}: salio > {lanzamiento}")

try:
    tot_lanza = int(input("Cuantas veces quieres lanza moneda? : "))
    lanzar_moneda(tot_lanza)
except ValueError:
    print("Error: Por favor, ingresa un número entero válido")
