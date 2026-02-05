"""
Ejercicio01 : Pedir a usuario que ingrese una oracion.
El programa debe devolver.
1.La oracion en mayusculas
2.Cuantas palabras tien la oracion.
3.Cual es el ultimo caracter de la oracion.
"""
#Ingreso
oración = input("Ingrese una oracion: ")

#Proceso
oracion_mayuscula =oración.upper()
oracion_palabras = len(oración.split())   #split cuenta palabras sin espacios
oracion_ultimaPalabra = oración[5]
#Salida 
print(f"En mayuscula: {oracion_mayuscula}")
print(f"Numero de palabras: {oracion_palabras}")
print(f"Ultima letra: {oracion_ultimaPalabra}")

