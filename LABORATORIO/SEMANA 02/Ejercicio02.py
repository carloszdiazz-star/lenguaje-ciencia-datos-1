"""
 Ejercicio02: Crear un programa que guarde el nombre de un producto
 y su precio en un diccionario.Calcular el precio final con un igv del 18%
 y agregarlo como valor del diccionario
"""
#Ingreso de datos
producto = {
    "nombre": "Laptop",
    "precio": 800
}

igv = 0.18 

#Proceso 
producto["precioFinal"] = producto["precio"] * (1+igv)

#Salida
print(f"Resumen compra: {producto["nombre"]}")
print(f"Total a pagar: {producto["precioFinal"]}")



