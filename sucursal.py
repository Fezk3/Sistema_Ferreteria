from lista_doble_C import ListaDobleCircular
from seccion import Seccion
class Sucursal:
    def __init__(self, ubicacion):
        self.id = 0
        self.ubicacion = ubicacion
        self.listaSeccion = ListaDobleCircular()
        self.id+=1

    def __repr__(self):
        salida=''
        salida += f'Identificacion {self.id}\n Ubicacion: {self.ubicacion}\n  Secciones de la sucursal: {self.listaSeccion.__repr__()}'
        return salida

    def agregaSeccion(self,seccion):
        self.listaSeccion.agregar(seccion)


    def agregaSeccionEspecifica(self, indice, seccion):
        numero = self.listaSeccion.num(indice)
        if numero != None:
            self.listaSeccion.insertar(seccion,numero)
        return numero

    def eliminarSeccion(self, indice):
        numero = self.listaSeccion.num(indice)
        if numero != None:
            self.listaSeccion.eliminar(numero)
        return numero

    def retornarSeccion(self, indice):
        numero = self.listaSeccion.num(indice)
        if numero != None:
            return self.listaSeccion.get(numero)
        return numero

