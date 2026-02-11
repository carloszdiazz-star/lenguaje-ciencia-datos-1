class Animal:
    
    def __init__(self,especie,edad):
        self.especie = especie
        self.edad = edad
    
    def ladrar(self):
        print("Animal planet....")
    def caminar(self):
        pass

    def describir(self):
        print(f"Soy un {self.especie} y tengo {self.edad} años")



class Perro(Animal):
      

      def ladrar(self):
        print("Guau guau")

objPerro = Perro("Perro",10)

objPerro.describir()
objPerro.ladrar()
#class Perro(Animal):
 #   pass
#class Gato(Animal):
  # pass
#print(Perro.__bases__) #Imprime la clase padre de Perro, en este caso es Animal
#print(Animal.__subclasses__()) #Imprime las clases hijas de Animal, en este caso son Perro y Gato