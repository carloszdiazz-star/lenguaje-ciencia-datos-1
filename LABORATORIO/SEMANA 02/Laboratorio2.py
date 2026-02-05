"""
La actividad consiste en desarrollar un programa en Python que simule la evaluacion de solicitudes de
prestamo en un banco. El estudiante debera utilizar variables, operadores logicos y condicionales para
determinar si un prestamo es aprobado o rechazado segun los ingresos del cliente, el monto solicitado
y su nivel de riesgo. A partir del codigo base proporcionado, el alumno debe modificarlo para calcular
el porcentaje del prestamo respecto a los ingresos, mostrar el monto de la cuota mensual
(considerando 12 meses y un interes anual del 5%) cuando el prestamo sea aprobado, y en caso de
rechazo, indicar el motivo principal ("alto riesgo" o "monto excesivo").
"""

# Ejemplo de referencia: evaluación simple de préstamo

# Entrada de datos
monto = float(input("Ingrese el monto solicitado: "))
ingreso = float(input("Ingrese los ingresos mensuales: "))
riesgo = input("Ingrese el nivel de riesgo (bajo, medio, alto): ").lower()

# Proceso
porcentaje = (monto / ingreso) * 100

if (riesgo == "bajo" or riesgo == "medio") and monto <= ingreso * 4:
    print("Préstamo aprobado")
    print("Porcentaje del préstamo respecto al ingreso: ", porcentaje, "%")

    total_pagar = monto * 1.05
    cuota = total_pagar / 12

    print("Monto de la cuota mensual:", cuota)
else:
    print("Préstamo rechazado")

    if riesgo == "alto":
        print("Motivo: alto riesgo")
    else:
        print("Motivo: monto excesivo")
