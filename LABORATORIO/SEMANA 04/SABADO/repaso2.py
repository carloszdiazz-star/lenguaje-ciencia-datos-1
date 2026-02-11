class Perro:
    especie = "mamifero" #atributos de clase

    def __init__(self,nombre,raza):
        
        #Atributos
        self.nombre = nombre
        self.raza = raza

    def ladrido(self):   #Siempre colocar el self cuando se crea algun meotodo
        print(f"{self.nombre} ladra Guau Guau")
    
    def caminar(self,pasos):
        print(f"{self.nombre} todos los dias camina {pasos} pasos")

objPerro = Perro("Bobby", "Pug")

objPerro.ladrido()
objPerro.caminar(150)

