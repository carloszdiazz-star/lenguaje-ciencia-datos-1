"""
 Ejercicio03: Crear una lista llamado invitados. Pida al usuario un nombre
 para decirle si esta en la lista o no .
"""
#Ingreso 
invitados = ["Juan", "Pedro", "Maria", "Luis"]
nombre = input("¿Cual es su nombre? ")

#Proceso
if nombre in invitados:
    mensaje = f"Bienvenido {nombre} estas en la lista"
    
else:
    mensaje = "Lo siento no estas invitado"

#Salida

print(mensaje)