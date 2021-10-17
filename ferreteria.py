from sucursal import Sucursal
from sucursal import Seccion
from seccion import tipoProducto


class Ferreteria:
    def __init__(self):
        self.listaSucursal = []
        self.cont = 0

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
            print('4 - Agregar elementos en sucursal')
            print('Para salir digite "salir"')
            opc = input('Que desea realizar?\n')

            if opc == "1":
                self.ingresarSucursal()
            if opc == "2":
                self.imprimirSucursal()
            if opc == "3":
                self.eliminar()
            if opc == "4":
                self.agregarEnSucursal()

    def ingresarSucursal(self):
        nombreSu = ""
        nombreSu = input("Digite la ubicacion de la sucursal\n")
        sucursal = Sucursal(nombreSu, self.cont)

        ciclo = 0
        ciclo2 = 0
        ciclo = input("cuantas secciones desea agregar: ")
        i = 0
        if not ciclo.isdigit():
            return
        while int(ciclo) > i:
            nombreSe = ""
            nombreSe = input("Digite el nombre de la seccion:\n")
            seccion = Seccion(nombreSe, i)
            i += 1

            ciclo2 = input("Cuantos tipos de productos desea agregar: ")
            if not ciclo2.isdigit():
                return
            j = int(ciclo2)
            while j > 0:
                tipo = ""
                tipo = input("Digite el nombre de tipo de productos que desea agregar:\n")
                tipoP = tipoProducto(tipo)
                seccion.agregarProducto(tipoP)
                j -= 1
            sucursal.agregaSeccion(seccion)

        self.listaSucursal.insert(self.cont, sucursal)
        self.cont += 1

    def eliminar(self):
        print('Que desea eliminar?')
        print('1 -Sucursal')
        print('2 -Seccion')
        print('3 -Tipo de producto')
        opc = ""
        opc = input("Elija una opcion: ")

        if not opc.isdigit():
            return f'Digito una opcion invalida'

        if opc == "1":
            print(self.eliminarSucursal())

        if opc == "2":
            print(self.eliminarSeccion())

        if opc == "3":
            print(self.eliminarTipo())


    def imprimirSucursal(self):
        for sucursal in self.listaSucursal:
            print(sucursal)

    def eliminarSucursal(self):
        self.imprimirSucursal()
        opc = input("Digite el id de la sucursal que desea elimjnar ")

        if not opc.isdigit() or int(opc) > len(self.listaSucursal):
            return f'Digito una opcion invalida'

        index = int(opc)
        del self.listaSucursal[index]
        return f'Sucursal eliminada exitosamente'

    def eliminarSeccion(self):
        self.imprimirSucursal()
        opc = input("Digite el id de la sucursal en la que esta la seccion que desea eliminar ")

        if not opc.isdigit() or int(opc) > len(self.listaSucursal):
            return f'Digito una opcion invalida'

        index = int(opc)
        print(self.listaSucursal[index])
        eliminado = input("digite la seccion que desea eliminar ")
        tam = self.listaSucursal[index].listaSeccion

        if not eliminado.isdigit() or int(eliminado) > tam.get_tamanio():
            return f'Digito una opcion invalida'

        self.listaSucursal[index].eliminarSeccion(int(eliminado))
        return f'Seccion eliminada exitosamente'

    def eliminarTipo(self):
        self.imprimirSucursal()
        opc = input("Digite el id de la sucursal ")

        if not opc.isdigit() or int(opc) > len(self.listaSucursal):
            return f'Digito una opcion invalida'

        index = int(opc)
        print(self.listaSucursal[index])
        seccion = input("digite la seccion donde se encuentra el tipo de producto ")
        tam = self.listaSucursal[index].listaSeccion

        if not seccion.isdigit() or int(seccion) > tam.get_tamanio():
            return f'Digito una opcion invalida'

        print(self.listaSucursal[index].retornarSeccion(int(seccion)))
        tipo = input('Digite el tipo de producto que desee eliminar ')

        if not opc.isdigit() or int(tipo) > tam.get_tamanio():
            return f'Digito una opcion invalida'

        self.listaSucursal[index].retornarSeccion(int(seccion)).eliminarTipo(int(tipo))
        return f'Tipo de producto eliminado exitosamente'

    def agregarEnSucursal(self):
        print()