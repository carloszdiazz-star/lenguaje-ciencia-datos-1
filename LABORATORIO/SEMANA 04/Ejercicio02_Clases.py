class Estudiante :
    def __init__(self,nombre,t1,t2,ef):  #Constructor
        self.nombre = nombre
        self.t1 = t1       #Datos estudiantes
        self.t2 = t2
        self.ef = ef
# Metodo para procesar promedio 
    def calcular_promedio(self):
        promedio = (self.t1 + self.t2 + self.ef)/3
        return promedio

    def mostrar_reporte(self):  #importante colocar self 
        print(f"El promedio de {self.nombre} es: {self.calcular_promedio():.2f}")




