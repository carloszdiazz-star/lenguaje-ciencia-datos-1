from vehiculos import Vehiculo

class Auto(Vehiculo):
    def __init__(self,placa,precioBase,puertas):
        super().__init__(placa,precioBase)
        self._puertas = puertas

    def calcular_alquiler(self, dias):
        total = super().calcular_alquiler(dias)

        if self._puertas > 2 :
            total+= (10*dias)
            return total 
        
class Moto(Vehiculo):
    def __init__(self,placa,precioBase,cc):
        super().__init__(placa,precioBase)
        self._cilindrada = cc

    def calcular_alquiler(self, dias):
        total = super().calcular_alquiler(dias)

        if self._cilindrada > 250 :
            total+= 5
            return total 