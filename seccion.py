from listadouble import ListaDobleEnlazada
from tipo_producto import tipoProducto


class Seccion:
    def __init__(self, nombre, numero):  # Madera Hierro
        self.numero = numero
        self.nombre = nombre
        self.listaTipoProductos = ListaDobleEnlazada()

    def __repr__(self):
        salida = ""
        salida += f'Numero: {self.numero}\ntipo: {self.nombre}\nproductos: {self.listaTipoProductos}\n'
        return salida

    def agregarProducto(self, producto):  # recibe un obj tipoProducto de file: Productos
        self.listaTipoProductos.agregar(producto)

    def agregarProductoEspecifico(self, producto, indice):
        self.listaTipoProductos.insertar(producto, indice)

    def eliminarTipo(self, indice):
        self.listaTipoProductos.eliminar(indice)

    def tamanioTipo(self):
        tam = self.listaTipoProductos.get_tamanio()
        return tam

    def retornaTipo(self, tipo):
        for n in self.listaTipoProductos.tamanio:
            if tipo is self.listaTipoProductos.get(n).tipoP:
                return self.listaTipoProductos.get(n)
        else:
            return None

    def muestra_tipo(self):

        for n in range(self.listaTipoProductos.tamanio):
            t_p = self.listaTipoProductos.get(n)
            print(f"{t_p.tipoP}")

    def llena_tipo_producto(self):

        tabla = tipoProducto("Tabla")
        tabla.llena_producto1("tablaPino")
        tabla.llena_producto2("tablaRoble")

        puerta = tipoProducto("Puerta")
        puerta.llena_producto1("puertaPino")
        puerta.llena_producto2("puertaRoble")

        perlin = tipoProducto("Hierro")
        perlin.llena_producto1("perlin")

        self.listaTipoProductos.agregar(tabla)  # tabla contiene las 2 pilas con las distintas tablas que hay
        self.listaTipoProductos.agregar(puerta)  # puerta contiene las 2 pilas con las distintas puertas que hay
        self.listaTipoProductos.agregar(perlin)
