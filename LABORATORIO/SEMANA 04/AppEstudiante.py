from EstudianteClass import Estudiante

#Entrdada de datos

nombre = input("Ingrese su nombre: ")
t1 = int(input("Ingrese la nota de su t1: "))
t2 = int(input("Ingrese la nota de su t2: "))
ef = int(input("Ingrese la nota de su EF: "))

#proceso 
objEstudiante = Estudiante(nombre,t1,t2,ef)
#objEstudiante.mostrar_reporte()

print(f"Tu promedio es : {objEstudiante.calcular_promedio():.2f}")

objEstudiante.mostrar_reporte()
