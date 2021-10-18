from sucursal import Sucursal
from sucursal import Seccion
from seccion import tipoProducto
from tipo_producto import Producto


class Ferreteria:
    def __init__(self):
        self.listaSucursal = []
        self.cont = 0

    def menuCompra(self):
        print("Digite el numero sucursal en la que desea realizar la compra:   ")
        for su in self.listaSucursal:
            print(f"1. Sucarsal de {su.nombre}")
        sucur = input()

        if not sucur.isdigit():
            return f'Digito una opcion invalida'

        #if int(sucur) > len(self.listaSucursal):
        #    return f'Digito una opcion invalida'

        if sucur == "1":
            self.menu_sucursal(1)
        elif sucur == "2":
            self.menu_sucursal(2)
        else:
            self.menu_sucursal(3)

    def menu_sucursal(self, n_su):
        print(f"Bienvenido a la sucursal de {self.listaSucursal[n_su].ubicacion}")
        print(f"Digite el numero de la seccion de la que desea ver los productos: ")
        for sel in self.listaSucursal[n_su].listaSeccion.tamanio:  # en base al tamanio
            print(f"Seccion de: {sel.retornarSeccion().nombre}")
        opci = input()

        if not opci.isdigit():
            return f'Digito una opcion invalida'

        if opci == "1":
            self.mostrar_maderas(n_su)
        elif opci == "2":
            self.mostrar_metales()
        else:
            return f'Digito una opcion invalida'

    def mostrar_maderas(self, n_su):  # muestra los tipos de producto
        madera = self.listaSucursal[n_su].retornarSeccion(0).retornaTipo("Madera")
        if madera.producto1.esta_vacia():
            pass
        else:
            print(f"{madera.producto1.top()}")

        if madera.producto2.esta_vacia():
            pass
        else:
            print(f"{madera.producto1.top()}")

    def mostrar_metales(self):
        pass

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

        ciclo = ''
        ciclo2 = ''
        ciclo3 = ''
        ciclo = input("cuantas secciones desea agregar: ")
        i = 0
        if not ciclo.isdigit():
            return f'Digito una opcion invalida'
        while int(ciclo) > i:
            nombreSe = ""
            nombreSe = input("Digite el nombre de la seccion:\n")
            seccion = Seccion(nombreSe, i)
            i += 1

            ciclo2 = input("Cuantos tipos de productos desea agregar: ")
            if not ciclo2.isdigit():
                return f'Digito una opcion invalida'
            j = int(ciclo2)
            while j > 0:
                tipo = ""
                tipo = input("Digite el nombre de tipo de productos que desea agregar:\n")
                tipoP = tipoProducto(tipo)

                nom = ""
                nom = input('Digite el nombre del producto\n')
                precio =""
                precio = input('Digite el precio de este producto\n')
                if not precio.isdigit():
                    return f'Digito una opcion invalida\n'
                cant = ""
                cant = input('Digite el stock de este producto\n')

                if not cant.isdigit():
                    return f'Digito una opcion invalida'
                l = 0
                while l < int(cant):
                    producto = Producto(nom,l,precio)
                    tipoP.agregaProducto(producto)
                    l+=1
                j -= 1


                seccion.agregarProducto(tipoP)

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
        print('Que desea agregar?')
        print('1 -Sucursal')
        print('2 -Seccion')
        print('3 -Tipo de producto')
        opc = ""
        opc = input("Elija una opcion: ")

        if not opc.isdigit():
            return f'Digito una opcion invalida'

        if opc == "1":
            print(self.agregarSucursal())

        if opc == "2":
            print(self.agregarSeccion())

        if opc == "3":
            print(self.agregarTipo())

    def agregarSucursal(self):
        nombre = ""
        nombre = input('Ingrese la ubicacion de la sucursal')
        sucursal =Sucursal(nombre, self.cont)
        self.listaSucursal.append(sucursal)
        cont+=1

    def agregarSeccion(self):
        self.imprimirSucursal()
        opc = input("Digite el id de la sucursal ")

        if not opc.isdigit() or int(opc) > len(self.listaSucursal):
            return f'Digito una opcion invalida'
        print(self.listaSucursal[int(opc)])
        #pos = ""

    def sucursalPorDefecto(self):
        sucursal = Sucursal('alajuela',0)
        seccion = Seccion('Madera',0)
        tipo = tipoProducto('Tabla')
        tipo2 = tipoProducto('Puerta')
        seccion.agregarProducto(tipo)
        seccion.agregarProducto(tipo2)
        seccion2 = Seccion('Hierro',1)
        tipo3 = tipoProducto('Perlin')
        seccion2.agregarProducto(tipo3)
        sucursal.agregaSeccion(seccion)
        sucursal.agregaSeccion(seccion2)