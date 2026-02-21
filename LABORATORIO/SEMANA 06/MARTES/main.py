
from modelos import Estudiante, Curso, Matricula

objEst = Estudiante()
objCur = Curso()
objMat = Matricula()

def menu():
    print("=======SISTEMAS DE MATRICULAS=======")
    print("1. Agregar Estudiante")
    print("2. Agregar curso")
    print("3. Matricular Estudiante en Curso")
    print("4. Ver reporte de Matrícula")
    print("5. Salir")
    return input("Seleccione una opcion: ")

while True: 
    op = menu()

    if op == "1":
        nom = input("El nombre del estudiante: ")
        objEst.insertar(nom)
        print("Estudiante registrado con exito")

    elif op == "2":
        nom = input("El nombre del curso: ")  
        objCur.insertar(nom)
        print("Curso registrado con exito")

    elif op == "3":
        print("---- Estudiantes ----")
        for e in objEst.listar():
            print(f"ID: {e[0]} - Nombre: {e[1]}")
    
        print("---- Cursos ----")
        for c in objCur.listar():
            print(f"ID: {c[0]} - Nombre: {c[1]}")

        id_est = input("Seleccione el ID del estudiante: ")
        id_cur = input("Seleccione el ID del curso: ")
        objMat.registrar_matricula(id_est,id_cur)
        print("Matrícula registrada con exito")

    elif op == "4":
        for m in objMat.listar_todo():
            print(f"Estudiante: {m[1]} - Curso: {m[2]}")

    elif op == "5":
        print("Saliendo...")
        break