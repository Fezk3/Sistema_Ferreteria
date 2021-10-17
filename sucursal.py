from lista_doble_C import ListaDobleCircular
from seccion import Seccion


class Sucursal:
    def __init__(self, ubicacion, numero):
        self.id = numero
        self.ubicacion = ubicacion
        self.listaSeccion = ListaDobleCircular()

    def __repr__(self):
        salida = ''
        salida += f'Identificacion {self.id}\nUbicacion: {self.ubicacion}\nSecciones de la sucursal: {self.listaSeccion.__repr__()}\n'
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


