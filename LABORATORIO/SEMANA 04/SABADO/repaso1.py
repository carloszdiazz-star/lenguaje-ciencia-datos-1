class Perro:
    def __init__ (self,nombre,raza):
        self.nombre = nombre
        self.raza = raza
        print(f"Soy un perro y mi nombre es {self.nombre} y soy de raza {self.raza}")

objPerro = Perro("Bobby", "Pug Carlino") #Instancia de clase perro 

print(objPerro.raza)
print(objPerro.nombre)
print(objPerro)