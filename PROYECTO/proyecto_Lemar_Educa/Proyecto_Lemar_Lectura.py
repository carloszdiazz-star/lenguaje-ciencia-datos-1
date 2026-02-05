import csv

alumnos = []

with open("evaluacion_lectora_lemar.csv", "r", encoding="utf-8-sig") as archivo:
    lector = csv.DictReader(archivo, delimiter=";")
    
    for fila in lector:
        alumnos.append(fila)
palabras_texto
print("Total de alumnos cargados:", len(alumnos))
print("Primer alumno:")
print(alumnos[0])
print("Último alumno:")
print(alumnos[-1])


alumnos_limpios = []

for alumno in alumnos:
    try:
        alumno["grado"] = int(alumno["grado"])
        alumno[""] = int(alumno["palabras_texto"])
        alumno["num_preguntas"] = int(alumno["num_preguntas"])
        alumno["comprension_pct"] = float(alumno["comprension_pct"])
        alumno["tiempo_seg"] = int(alumno["tiempo_seg"])
        
        # convertir coma decimal a punto
        alumno["velocidad_ppm"] = float(
            alumno["velocidad_ppm"].replace(",", ".")
        )

        alumnos_limpios.append(alumno)

    except ValueError:
        # si algún dato está mal, se ignora el registro
        continue

    print("Alumnos válidos:", len(alumnos_limpios))
print("Ejemplo alumno limpio:")
print(alumnos_limpios[0])   





