def calcular_promedio(t1,t2,ef):
    prom = (t1 + t2+ ef) / 3
    return prom

print("---SISTEMA DE PROMEDIOS---")
nombre = input("Ingrese su nombre: ")
t1 = float(input("Ingrese nota de su T1: "))
t2 = float(input("Ingrese nota de su T2: "))
ef = float(input("Ingrese nota de su Examen final: "))

prom_estudiante = calcular_promedio(t1,t2,ef)

print(f"{nombre},Tu Promedio es de = {prom_estudiante:.2f}")