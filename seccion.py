class Seccion:
    def __init__(self, numero, nombre):
        self.numero=numero
        self.nombre=nombre

    def __repr__(self):
        salida=""
        salida+= f'Numero: {self.numero}\n tipo: {self.nombre}'
        return salida

