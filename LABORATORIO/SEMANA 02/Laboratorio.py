"""
 Laboratorio:
 Modifica el código para que el programa reciba los ingresos de cinco sucursales, calcule el total y el
promedio general, y muestre un mensaje según el resultado: "Excelente rendimiento" si el promedio
supera los S/70,000, "Rendimiento aceptable" si está entre S/40,000 y S/70,000, y "Rendimiento bajo"
si es menor a S/40,000.
"""


# Ejemplo de referencia: cálculo de ingresos promedio

# Entrada de datos
sucursal1 = float(input("Ingrese el ingreso de la sucursal 1: "))
sucursal2 = float(input("Ingrese el ingreso de la sucursal 2:"))
sucursal3 = float(input("Ingrese el ingreso de la sucursal 3: "))
sucursal4 = float(input("Ingrese el ingreso de la sucursal 4: "))
sucursal5 = float(input("Ingrese el ingreso de la sucursal 5: "))

# Proceso
total = sucursal1 + sucursal2 + sucursal3 +sucursal4 + sucursal5
promedio = total / 5

# Salida de resultados
print (f"Ingreso total: {total}")
print (f"Promedio de ingresos: {promedio}")

if promedio > 70000:
    print ("Excelente rendimiento")
elif promedio >= 40000 and  promedio <= 70000:
    print ("Rendimiento aceptable")
else:
    print ("Rendimiento bajo")