class Vehiculo:
    def __init__(self,placa,precioBase):
        self._placa = placa
        self._precioBase = precioBase

    @property
    def precio_base(self):
        return self._precioBase
    
    @precio_base.setter
    def precio_base(self,valor):
        self._precioBase = valor

    def calcular_alquiler(self,dias):
        return self._precioBase * dias
        