from listadouble import ListaDobleEnlazada
from tipo_producto import tipoProducto


class Seccion:
    def __init__(self, nombre, numero):
        self.numero = numero
        self.nombre = nombre
        self.listaProductos = ListaDobleEnlazada()

    def __repr__(self):
        salida = ""
        salida += f'Numero: {self.numero}\ntipo: {self.nombre}\nproductos: {self.listaProductos}\n'
        return salida

    def agregarProducto(self, producto):
        self.listaProductos.agregar(producto)

    def agregarProductoEspecifico(self, producto, indice):
        if indice < self.listaProductos.cantidad_nodos:
            numero = self.listaProductos.insertar(producto, indice)

    def eliminarTipo(self, indice):
        self.listaProductos.eliminar(indice)

    def tamanioTipo(self):
        tam = self.listaProductos.get_tamanio()
        return tam