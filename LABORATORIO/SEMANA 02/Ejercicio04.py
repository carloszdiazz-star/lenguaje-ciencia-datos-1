"""
 Ejercicio04: Conversor de unidades (pies -> metros)
 Usando las tuplas (ya que no deben cambiar)
 Pedir al usuario una cantidad en metros y mostrarla en pies.

"""

#Ingreso
CONVERSION = (3.28084, 0.3048)
metros = float(input("Ingrese una cantidad en metros: "))

#Proceso
pies = metros * CONVERSION[0]
pulgadas = metros * CONVERSION[1]

#SALIDA
print(f"{metros} metros son {pies} pies")
print(f"{metros} metros son {pulgadas} pulgadas")