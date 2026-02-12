from empleado import Empleado

#Hijo 01
class Empleado_fijo(Empleado):
      def __init__(self,nombre,bono,sueldo_mensual):
            super().__init__(nombre,bono)
            self.sueldo_mensual = sueldo_mensual
      
      def calcular_total(self):
            return self.calcular_pago_final(self.sueldo_mensual)


#Hijo 02
class Empleado_porHoraas(Empleado):
      def __init__(self, nombre, bono,horas,tarifa):
            super().__init__(nombre, bono)
            self.horas = horas
            self.tarifa = tarifa
      
      def calcular_total(self):
            pago = self.tarifa * self.horas
            return self.calcular_pago_final(pago)

                 

