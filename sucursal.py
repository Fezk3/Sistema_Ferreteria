from lista_doble_C import ListaDobleCircular
from seccion import Seccion
from cola_clientes import ColaClientes
from time import sleep
from factura import Factura
from sucursal import Seccion
from seccion import tipoProducto

class Sucursal:
    def __init__(self, ubicacion, numero):
        self.id = numero
        self.ubicacion = ubicacion
        self.listaSeccion = ListaDobleCircular()
        self.caja = ColaClientes()  # ya tiene un cliente dentro

        # atributos de todo
        self.seccion = Seccion('Madera',0)
        self.tipo = tipoProducto('Tabla')
        self.tipo2 = tipoProducto('Puerta')
        self.tipo.llena_producto1('tablaPino')
        self.tipo.llena_producto2('tablaRoble')
        self.tipo2.llena_producto1('puertaPino')
        self.tipo2.llena_producto2('puertaRoble')
        self.seccion.agregarProducto(self.tipo)
        self.seccion.agregarProducto(self.tipo2)
        self.seccion2 = Seccion('Hierro',1)
        self.tipo3 = tipoProducto('Perlin')
        self.tipo3.llena_producto1('perlin')
        self.seccion2.agregarProducto(self.tipo3)

        self.agregaSeccion(self.seccion)
        self.agregaSeccion(self.seccion2)

    def __repr__(self):
        salida = ''
        salida += f'Identificacion {self.id}\nUbicacion: {self.ubicacion}\nSecciones de la sucursal: {self.listaSeccion}\n'
        # salida +=
        return salida

    def agregaSeccion(self, seccion):
        self.listaSeccion.agregar(seccion)

    def agregaSeccionEspecifica(self, indice, seccion):
        self.listaSeccion.insertar(seccion, indice)

    def eliminarSeccion(self, indice):
        self.listaSeccion.eliminar(indice)

    def retornarSeccion(self, indice):
        return self.listaSeccion.get(indice)

    def muestra_secciones(self):
        print(f" {self.listaSeccion}\n")

    def atiende_cliente(self, cliente):
        factura = Factura()
        print("Esperando a que el cliente de adelante termine de ser atendido")
        self.caja.agregar_cliente(cliente)
        sleep(8)
        for cl in self.caja.cola_clientes:  # por cada cliente en la cola
            for item in range(cl.carrito.tamnaio()):
                factura.recibe_item_comprado(cl.saca_producto_carrito())  # saca del carrito y aniade a factura
            print("Factura generada: ")
            factura.muestra_factura()
            factura.guarda_en_archivo()
        self.caja.sacar_cliente()  # saca solo si la lista no esta vacia
        self.caja.sacar_cliente()
