saldo = 1000.0

while True:
    print("\n1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        print(f"Saldo: s/. {saldo:.2f}")

    elif opcion == "2":
        monto = float(input("Monto a retirar: s/. "))

        if monto > saldo:
            print("Saldo insuficiente")
        elif monto <= 0:
            print("Monto inválido")
        else:
            saldo -= monto
            print(f"Nuevo saldo: s/. {saldo:.2f}")

    elif opcion == "3":
        break
