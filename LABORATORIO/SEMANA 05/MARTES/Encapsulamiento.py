
"""
class Clase:
    __atributi_clase = "Hola"   #Poner dos guiones hace el atributo privado .

    def __init__(self,atributo_instancia):
        self.atributo_instancia = atributo_instancia

        
#------------------------------------

mi_objeto = Clase("Que tal")
print(mi_objeto.atributi_clase)
print(mi_objeto.atributo_instancia)
"""

class Clase:
    atributo_clase = "Esto es un atributo de clase Public"
    __atributo_clase = "Esto es un atributo de clase privado"

    def mi_metodo(self):
        self.__variable = 5+5

    def acceso(self):
        return self.__variable
    
    @property
    def mostrar(self):
        return self.__atributo_clase
    
    @mostrar.setter
    def modificar(self,nueva):
        self.__atributo_clase = nueva



#-*---------*****************

p = Clase()
p.mi_metodo()          # 🔥 Crear la variable
p.modificar = "Bobby"
print(p.mostrar)

