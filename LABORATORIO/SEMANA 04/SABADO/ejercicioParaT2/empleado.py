class Empleado:
    def __init__(self,nombre,bono):
        self.nombre = nombre
        self.bono = bono


    def calcular_pago_final(self,sueldo):
        return sueldo + self.bono
    
    def mostrar_resultado(self):
        return f"Empleado {self.nombre} ---- Bono aplicado {self.bono} "
      
