class Producto:
    def __init__(self, nombre, id, precio):
        self.nombre = nombre
        self.id = id
        self.precio = precio

    def __repr__(self):
        salida=''
        salida=f'\nnombre: {self.nombre} \nid: {self.id} \nprecio: {self.precio}'
        return salida