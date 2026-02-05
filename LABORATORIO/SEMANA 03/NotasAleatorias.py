"""
Indicaciones:
1. Usa el módulo random.
2. Crea una función llamada generar_notas(cantidad) que:
   - Genere una nota aleatoria entre 0 y 20 para cada estudiante.
   - Muestre en pantalla la nota de cada estudiante.
3. El programa debe pedir al usuario cuántos estudiantes hay.
4. Al finalizar, el programa debe mostrar:
   - El promedio de las notas.
   - La nota más alta y la más baja.
5. Usa try/except para validar que el usuario ingrese un número válido.
6. Si el usuario ingresa 0 o un número negativo, muestra un mensaje de error.
"""

import random
notas_es =[]
def generar_notas(estudiantes):
    for i in range(estudiantes):
        notas = random.randint(0,20)
        notas_es.append(notas)
        print(f"Nota de Estudiante {i+1}: {notas}")

print("Ingrese numero de estudiantes")

try :
    cantidad = int(input("Ingrese cantidad: "))
    if cantidad <=0 :
        print("Ingrese un valor valido")
    else :
        generar_notas(cantidad)
        sumaNotas = sum(notas_es)
        promNotas = sumaNotas / len(notas_es)
        notaAlta = max(notas_es)
        notaBaja = min(notas_es)
        print(f"Suma de todas las notas: {sumaNotas} ")
        print(f"Promedio notas: {promNotas}")
        print(f"Nota mas alta: {notaAlta}")
        print(f"Nota mas baja: {notaBaja}")
except ValueError:
    print("Error: Por favor, ingresa un número entero válido")


    
    

    
