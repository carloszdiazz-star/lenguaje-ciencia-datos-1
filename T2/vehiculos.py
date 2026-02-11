# CLASE BASE (PADRE)
class Vehiculo:
    def __init__(self, placa, precio_base):
        self._placa = placa 
        self._precio_base = precio_base

    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor):
        self._precio_base = valor

    def calcular_alquiler(self, dias):
        return self._precio_base * dias

# CLASE HIJA: AUTO
class Auto(Vehiculo):
    def __init__(self, placa, precio_base, puertas):
        super().__init__(placa, precio_base)
        self.puertas = puertas

    def calcular_alquiler(self, dias):
        total = super().calcular_alquiler(dias)
       
        if self.puertas > 2:
            total += (10 * dias)
        return total

# CLASE HIJA: MOTO
class Moto(Vehiculo):
    def __init__(self, placa, precio_base, cilindrada):
        super().__init__(placa, precio_base)
        self.cilindrada = cilindrada

    def calcular_alquiler(self, dias):
        total = super().calcular_alquiler(dias)
      
        if self.cilindrada > 250:
            total += 5
        return total