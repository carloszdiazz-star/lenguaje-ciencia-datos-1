



def celcius_far(c):
    
    return (c * 9/5) + 32

def far_celcius(f):

    return (f-32) * 5/9

print("1. Convertir de Celsius a Fahrenheit")
print("2. Convertir de Fahrenheit a Celsius")

try :
    opcion = int(input("Ingrese la opcion deseada: "))
    
    if opcion == 1:
        valor_conversion = float(input("Ingrese el valor a conversion:"))
        print(f"La conversion de Celsius a Fahrenheit es: {celcius_far(valor_conversion):.2f}")
    elif opcion ==2:
        valor_conversion = float(input("Ingrese el valor a conversion:"))
        print(f"La conversion de Fahrenheit a Celsius es: {far_celcius(valor_conversion):.2f}")

    else :
        print("Ingresa un valor valido")

except ValueError:
    print("Valor no valido, ingresa un numero!")

        