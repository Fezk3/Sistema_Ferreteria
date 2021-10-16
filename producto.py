from misc import Misc


class Producto(Misc):
    def __init__(self, nombre, id, precio):
        self.nombre = nombre
        self.id = id
        self.precio = precio

    def __repr__(self):
        salida=''
        salida=f'nombre: {self.nombre} \n id: {self.id} \n  precio: {self.precio}'
        return salida