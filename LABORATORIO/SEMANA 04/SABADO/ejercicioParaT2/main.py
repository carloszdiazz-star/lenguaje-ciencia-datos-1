from tipo_Empleado import Empleado_fijo, Empleado_porHoraas

print("======== Sistema de Planilla ==================")
nombre =input("Ingrese nombre de empleado: ")
bono = float(input("Ingrese bono: "))

print("SELECCIONE EL TIPO DE EMPPLEADO")
print("Opcion 1 : Empleado fijo")
print("Opcion 2 : Empleado por horas")
opcion = int(input("Ingrese #opcion: "))

if opcion == 1:
    sueldo = float(input("Ingrese sueldo: "))
    objEmpleado = Empleado_fijo(nombre,bono,sueldo)
    print("----Mostrar Resultados-----")
    print(objEmpleado.mostrar_resultado())
    print(f"Tu sueldo total es : {objEmpleado.calcular_total()}")

elif opcion == 2:
    horas = float(input("Ingrese las horas trabajadas: "))
    tarifa = float(input("Ingrese su tarifa por hora: "))
    objEmpleado = Empleado_porHoraas(nombre,bono,horas,tarifa)
    print("----Mostrar Resultados-----")
    print(objEmpleado.mostrar_resultado())
    print(f"Tu sueldo total es : {objEmpleado.calcular_total()}")

else :
    print("Ingrese una ocpion valida !")



    

    
   
    

