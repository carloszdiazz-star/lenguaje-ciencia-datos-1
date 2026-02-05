# Sistema de login con una base de datos (Diccionario) con tres intentos de bloqueo

usuarios_registrados = [
    {"usuario": "admin", "contrasena": "admin123"},    
    {"usuario": "Luis", "contrasena": "pass1"},
    {"usuario": "Maria", "contrasena": "pass2"}                                                                                                                    
]
intentos = 3
acceso_concedido = False

print("Bienvenido al sistema de login")
usuario_imput = input("Ingrese su nombre de usuario: ")
contrasena_imput = input("Ingrese su contraseña: ")

for cuenta in usuarios_registrados:
    if cuenta["usuario"] == usuario_imput and cuenta["contrasena"] == contrasena_imput:
        acceso_concedido = True
        break

if acceso_concedido:
    print(f"Bienvenido al sistema")
else:
    print("Acceso denegado")