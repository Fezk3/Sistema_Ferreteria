from listadouble import ListaDobleEnlazada

class tipo_productos:

    def __init__(self, tipo):
        self.tipo = tipo
        self.lista_de_tipos = ListaDobleEnlazada()  # va a contener los obj tipoProducto
