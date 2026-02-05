#Ejercicios 01 : List
areas = ["matematica", "fisica", "quimica"]
areas.append("biologia")  #append = agregar 
print(areas)

#Ejercicio 02 : tupla
coordenadas = (10,50) #I(x,Y)
#coordenadas[0] = 20

#Ejercicio 03 : diccionario
estudiantes = {
    "nombre": "Jean",
    "edad": 35,
    "carreras": ["Ingenieria","Arquitectura"]

}

print(estudiantes["carreras"])

estudiantes = {
    "nombre": "Jean",
    "edad": 35,
    "notas": [10,20,15]

}

print(f"Nota mas alta: {max(estudiantes['notas'])} ")

