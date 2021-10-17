from sucursal import Sucursal
from sucursal import Seccion
from seccion import tipoProducto


class Ferreteria:
    def __init__(self):
        self.listaSucursal = []
        self.cont =0

    def agregarSucursales(self, sucursal):
        self.listaSucursal.alfinal(sucursal)

    def eliminarSucursales(self, id):
        self.listaSucursal.Remover(id)

    def SeccionESpecifica(self, id):
        self.listaSucursal.get(id)

    def menuPrincipal(self):
        opc = ""
        print('\n\t\t\tBienvenido Amigo al Martillazo Feliz!!')
        while opc != "salir":
            print('\n\n1 - Agregar una sucursal')
            print('2 - Ver las sucursales')
            print('3 - Eliminar')
            print('Para salir digite "salir"')
            opc = input('Que desea realizar?\n')

            if opc == "1":
                self.ingresarSucursal()
            if opc == "2":
                self.imprimirSucursal()
            if opc == "3":
                self.eliminar()

    def ingresarSucursal(self):
        nombreSu = ""
        nombreSu = input("Digite la ubicacion de la sucursal\n")
        sucursal = Sucursal(nombreSu, self.cont)

        ciclo = 0
        ciclo2 = 0
        ciclo = int(input("cuantas secciones desea agregar: "))
        i=0
        while ciclo > i:
            nombreSe = ""
            nombreSe = input("Digite el nombre de la seccion:\n")
            seccion = Seccion(nombreSe, i)
            i+=1

            ciclo2 = int(input("Cuantos tipos de productos desea agregar: "))
            while ciclo2 > 0:
                tipo = ""
                tipo = input("Digite el nombre de tipo de productos que desea agregar:\n")
                tipoP = tipoProducto(tipo)
                seccion.agregarProducto(tipoP)
                ciclo2 -= 1
            sucursal.agregaSeccion(seccion)

        self.listaSucursal.insert(self.cont,sucursal)
        self.cont+=1
    def eliminar(self):
        print('Que desea eliminar?')
        print('1 -Sucursal')
        print('2 -Seccion')
        print('3 -Tipo de producto')
        print('4 -Producto')
        opc= ""
        opc = input("Elija una opcion: ")
        if not opc.isdigit():

            return
        if opc == "1":
            self.imprimirSucursal()
            opc= input("Digite el id de la sucursal que desea elimjnar")
            if opc.isdigit():

                return
            self.listaSucursal.Remover(opc)
        if opc == "2":
            print("")
        if opc == "3":
            print("")
        if opc == "4":
            print("")

    def imprimirSucursal(self):
        for sucursal in self.listaSucursal:
            print(sucursal)