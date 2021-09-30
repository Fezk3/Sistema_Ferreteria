from misc import Misc


class Cliente(Misc):
    
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.carrito = []

