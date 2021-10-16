from listadouble import ListaDobleEnlazada
from tipo_producto import tipoProducto


class Seccion:
    def __init__(self, nombre):
        self.numero = 0
        self.nombre = nombre
        self.listaProductos = ListaDobleEnlazada()
        self.numero += 1

    def __repr__(self):
        salida = ""
        salida += f'Numero: {self.numero}\n tipo: {self.nombre}\n productos: {self.lista.__repr__()}'
        return salida

    def agregarProducto(self, producto):
        self.listaProductos.agregar(producto)

    def agregarProductoEspecifico(self, producto, indice):
        if indice < self.listaProductos.cantidad_nodos:
            numero = self.listaProductos.insertar(producto, indice)

    def eliminarSeccion(self, indice):
        self.listaProductos.get(indice)
