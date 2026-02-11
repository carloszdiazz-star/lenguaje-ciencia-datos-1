from vehiculos import Auto, Moto

print("======== Sistema de Flota 'Móvil' ==============")
placa = input("Ingrese la placa del vehículo: ")
precio_base = float(input("Ingrese el precio base de alquiler por día: "))
dias = int(input("Ingrese la cantidad de días de alquiler: "))

print("\nSeleccione el tipo de vehículo:")
print("1. Auto")
print("2. Moto")
opcion = input("Ingrese la opción: ")

objVehiculo = None 

if opcion == "1":
    puertas = int(input("Ingrese el número de puertas: "))
    objVehiculo = Auto(placa, precio_base, puertas)

elif opcion == "2":
    cilindrada = int(input("Ingrese la cilindrada (cc): "))
    objVehiculo = Moto(placa, precio_base, cilindrada)

else:
    print("Opción inválida.")

if objVehiculo:
    total_pagar = objVehiculo.calcular_alquiler(dias)
    print("\n=== RESUMEN DE ALQUILER ====")
    print(f"Placa del vehículo: {objVehiculo._placa}")
    print(f"Total a pagar: S/. {total_pagar:.2f}")