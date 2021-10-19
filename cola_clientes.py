from cliente import Cliente
from producto import Producto


class ColaClientes:

    def __init__(self):
        self.cola_clientes = []
        # esto para que cada cola de clientes tenga uno frente al user
        c = Cliente()
        c.carrito.agreagar(Producto("Puerta Pino", "6", 90000))
        self.agregar_cliente(c)

    def agregar_cliente(self, clien):
        self.cola_clientes.append(clien)

    def sacar_cliente(self):
        if self.esta_vacia() is not True:
            self.cola_clientes.pop(0)

    def esta_vacia(self):
        return self.cola_clientes == []

    def get_tamanio(self):
        return len(self.cola_clientes)

