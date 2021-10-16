from listasimple import ListaSimple
from sucursal import Sucursal
from sucursal import Seccion
from seccion import tipoProducto


class Ferreteria:
    def __init__(self):
        self.listaSucursal = ListaSimple()

    def agregarSucursales(self, sucursal):
        self.listaSucursal.alfinal(sucursal)

    def eliminarSucursales(self, id):
        self.listaSucursal.Remover(id)

    def SeccionESpecifica(self, id):
        self.listaSucursal.get(id)

    def menuPrincipal(self):
        opc=""
        print('\n\t\t\tBienvenido Amigo al Martillazo Feliz!!')
        while opc != "salir":
            print('\n\n1- Agregar una sucursal')
            print('2- Ver las sucursales')
            print('Para salir digite "salir"')
            opc=input('Que desea realizar?\n')

            if opc == "1":
                self.ingresarSucursal()
            if opc == "2":
                print(self.listaSucursal.__repr__())

    def imprimirFerreteria(self):
        self.listaSucursal.__repr__()
    def ingresarSucursal(self):
        nombreSu = ""
        nombreSu = input("Digite la ubicacion de la sucursal\n")
        sucursal = Sucursal(nombreSu,1)

        ciclo = 0
        ciclo2 = 0
        ciclo = int(input("cuantas secciones desea agregar: "))
        while ciclo > 0:
            nombreSe = ""
            nombreSe = input("Digite el nombre de la seccion:\n")
            seccion = Seccion(nombreSe,ciclo)
            ciclo -= 1

            ciclo2 = int(input("Cuantos tipos de productos desea agregar: "))
            while ciclo2 > 0:
                tipo = ""
                tipo = input("Digite el nombre de tipo de productos que desea agregar:\n")
                tipoP = tipoProducto(tipo)
                seccion.agregarProducto(tipoP)
                ciclo2 -= 1
            sucursal.agregaSeccion(seccion)

        self.listaSucursal.alfinal(sucursal)
