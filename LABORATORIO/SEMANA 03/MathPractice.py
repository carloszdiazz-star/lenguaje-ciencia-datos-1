
"""
Diseña un programa en Python que permita calcular el perímetro de un 
círculo o el área de un cuadrado utilizando funciones y el módulo math. El 
programa debe mostrar un menú de opciones al usuario, solicitar el
valor correspondiente (radio o lado), aplicar la fórmula matemática
adecuada y mostrar el resultado con dos decimales. Además, se debe validar 
la entrada del usuario para evitar errores y opciones no válidas.
"""


import math

def peri_circulo(radio) :
    return 2*math.pi*radio

def area_cuadrado(lado) :
    return math.pow(lado,2)

print("1.Hallar perimetro circulo.")
print("2.Hallar Area cuadrado.")



try:
   opcion = int(input("Ingrese la opcion:"))
   r_l = float(input("ingrese el radio o lado:"))  

   if opcion == 1 :
      print(f"El perimetro del circulo es {peri_circulo(r_l):.2f}")
   elif opcion == 2 :
      print(f"El area del cuadrado es {area_cuadrado(r_l):.2f}")
   else :
      print("Ingrese un valor valido !")

except ValueError:
   print("Error: Por favor, ingresar valores numéricos bastardo!")