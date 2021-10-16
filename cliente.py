from pila import Pila


class Cliente:

    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.carrito = Pila()  # se aniadiran los productos de las pilas que los contienen en la ferreteria

    def agregar_producto_carrito(self, prod):
        self.carrito.agreagar(prod)
        print(f"Elemento agregado al carrito: {prod}")

    def total_carrito(self):
        total = 0
        for n in self.carrito.items:
            total += n.precio

        return total

    def saca_producto_carrito(self):
        return self.carrito.sacar()  # para la info de la factura

