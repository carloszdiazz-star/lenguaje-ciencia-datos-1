"""
TipoMetodos:
1. Metodos de instancia (self) metodo()
2.Metodos de clase (cls) @classmethod
3. Metodos estaticos @staticmethod
"""

class Producto :
    def metodo_instancia(self):
        print("Este es un método de instancia")

    @classmethod
    def metodo_clase(cls):
        print("Este es un método de clase")

    @staticmethod
    def metodo_estatico():
        print("Este es un método estático")

print(Producto.metodo_estatico())
print(Producto.metodo_clase())